# This file is part of AdMincer,
# Copyright (C) 2019 eyeo GmbH
#
# AdMincer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# AdMincer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with AdMincer. If not, see <http://www.gnu.org/licenses/>.

"""Tests for the CLI."""

import fnmatch
import glob
import os
import random

from PIL import Image, ImageDraw
import pytest

import admincer.index as idx

from conftest import make_image, Colors as cc
from test_slice import SLICE_EXPECT, check_results


def test_noargs(script_runner):
    """Show brief usage info when called with no arguments."""
    ret = script_runner.run('admincer')
    assert not ret.success
    assert 'Batch image editor' in ret.stdout
    assert ret.stderr == ''


@pytest.fixture()
def fragdir2(tmpdir):
    """Two more directories with fragments."""
    ret = tmpdir.mkdir('fragdir2')
    make_image(ret.mkdir('1').join('blue.gif'), 10, 10, cc.BLUE)
    make_image(ret.mkdir('2').join('pink.gif'), 10, 10, cc.PINK)
    return ret


@pytest.fixture()
def regdir2(tmpdir):
    """One image with several regions for test_place()."""
    ret = tmpdir.mkdir('regdir2')
    make_image(ret.join('img.png'), 200, 200, cc.WHITE)
    ret.join('index.csv').write('\n'.join([
        'image,xmin,ymin,xmax,ymax,label',
        'img.png,0,0,10,24,a',
        'img.png,10,0,40,40,a',
        'img.png,40,0,90,60,a',
        'img.png,0,100,10,110,b'
    ]))
    return ret


@pytest.fixture()
def check_log(logs_dir):
    """Check logs against expected outputs with filename pattern matching."""

    def checker(output, log_name):
        """Compare output to lines read from log_name with fnmatch."""
        expect_output = logs_dir.join(log_name).read().splitlines()
        got_output = output.splitlines()
        assert len(expect_output) == len(got_output)
        for got, expect in zip(got_output, expect_output):
            assert fnmatch.fnmatch(got, expect)

    return checker


def test_place(script_runner, tmpdir, regdir2, fragdir, fragdir2):
    """Place fragments onto a source image."""
    targetdir = tmpdir.join('output')
    ret = script_runner.run(
        'admincer', 'place',
        '--fragments', 'a=' + str(fragdir),
        # Test providing multiple directories for the same region type.
        '-f', 'b={}:{}'.format(fragdir2.join('1'), fragdir2.join('2')),
        '-n', '10',
        str(regdir2), str(targetdir),
    )
    assert ret.success
    assert ret.stdout == ''
    assert ret.stderr == ''
    outputs = [
        Image.open(img_path)
        for img_path in glob.glob(os.path.join(str(targetdir), '*.png'))
    ]
    # Identify unique combinations of colors in the four regions.
    signatures = {
        tuple(o.getpixel(p) for p in [(1, 22), (11, 1), (41, 1), (1, 101)])
        for o in outputs
    }
    # Since the first three regions only have one candidate fragment, there are
    # only two possibilities for the complete signature.
    assert signatures == {
        (cc.RED, cc.GREEN, cc.ORANGE, cc.BLUE),
        (cc.RED, cc.GREEN, cc.ORANGE, cc.PINK),
    }
    assert targetdir.join('regions.csv').check(file=1)


def test_place_verbose(script_runner, tmpdir, regdir2, fragdir, fragdir2,
                       check_log):
    """Place fragments with verbose output."""
    targetdir = tmpdir.join('output')
    random.seed(0)  # To prevent variation in placement order.
    ret = script_runner.run(
        'admincer', 'place',
        '--verbose',
        '-f', 'a=' + str(fragdir),
        '-f', 'b=' + str(fragdir),
        '-n', '2',
        str(regdir2), str(targetdir),
    )
    assert ret.success
    assert ret.stdout == ''
    check_log(ret.stderr, 'place-v.log')


@pytest.fixture()
def regdir3(tmpdir):
    """Image with three regions of the same size."""
    ret = tmpdir.mkdir('regdir3')
    make_image(ret.join('img.png'), 12, 12, cc.WHITE)
    ret.join('index.csv').write('\n'.join([
        'image,xmin,ymin,xmax,ymax,label',
        'img.png,0,0,10,10,a',
        'img.png,0,0,8,8,b',
        'img.png,0,0,12,12,c',
    ]))
    return ret


def test_place_resize_modes(script_runner, tmpdir, regdir3, fragdir2):
    """Place fragments with different resize modes."""
    targetdir = tmpdir.join('output')
    ret = script_runner.run(
        'admincer', 'place',
        '-f', 'a=' + str(fragdir2),
        '-f', 'b=' + str(fragdir2),
        '-f', 'c=' + str(fragdir2),
        '--resize-mode', 'scale',
        '--resize-mode', 'b=pad',
        '--resize-mode', 'c=crop',
        str(regdir3), str(targetdir),
    )
    assert ret.success
    assert ret.stdout == ''
    assert ret.stderr == ''


def test_invalid_resize_mode(script_runner, tmpdir, regdir3, fragdir2):
    ret = script_runner.run(
        'admincer', 'place',
        '-f', 'a=' + str(fragdir2),
        '-f', 'b=' + str(fragdir2),
        '-f', 'c=' + str(fragdir2),
        '-r', 'foobar',
        str(regdir3), str(tmpdir),
    )
    assert not ret.success
    assert ret.stdout == ''
    assert 'must be "scale", "pad" or "crop"' in ret.stderr


def test_extract(script_runner, tmpdir, regdir):
    """Extract regions into a separate directory."""
    r0 = tmpdir.join('r0')
    r1 = tmpdir.join('r1')
    r2 = tmpdir.join('r2')
    ret = script_runner.run(
        'admincer', 'extract',
        '--target-dir', 'r1=' + str(r1),
        '-t', 'r2=' + str(r2),
        '-t', 'r0=' + str(r0),
        str(regdir),
    )

    assert ret.success
    assert ret.stdout == ''
    assert ret.stderr == ''

    # Check that output files were created. We don't check the content of the
    # files here because there's test_extract.py.
    assert r0.check(dir=1)
    assert len(list(r0.visit())) == 0
    assert len(list(r1.visit())) == 3
    assert len(list(r2.visit())) == 1


def test_extract_debug(script_runner, tmpdir, regdir, check_log):
    """Extract regions with verbose output."""
    r0 = tmpdir.join('r0')
    r1 = tmpdir.join('r1')
    r2 = tmpdir.join('r2')
    ret = script_runner.run(
        'admincer', 'extract',
        '-vv',
        '-t', 'r0=' + str(r0),
        '-t', 'r1=' + str(r1),
        '-t', 'r2=' + str(r2),
        str(regdir),
    )

    assert ret.success
    assert ret.stdout == ''
    check_log(ret.stderr, 'extract-vv.log')


def test_find_region(script_runner, regdir):
    """Find screenshots with marked regions of specific type and size."""
    ret = script_runner.run(
        'admincer', 'find',
        '--region=r1:10x10',
        '-r', 'r3:30x100:100',
        str(regdir),
    )

    assert ret.success
    assert ret.stdout == 'blue3.png\n'


def test_find_fragment(script_runner, fragfind_dir):
    """Find screenshots with specific fragments."""
    needles_dir = fragfind_dir.join('needles')
    ret = script_runner.run(
        'admincer', 'find',
        '--fragment={}'.format(needles_dir.join('2.png')),
        '-f', '{}:5'.format(needles_dir.join('3.png')),
        str(fragfind_dir.join('haystack')),
    )

    assert ret.success
    assert ret.stdout == '1.jpg\n'


def test_find_region_no_index(script_runner, fragfind_dir):
    """Error when --region is given but there's no region index."""
    needles_dir = fragfind_dir.join('needles')
    ret = script_runner.run(
        'admincer', 'find',
        '-r', 'r1:30x100',
        str(needles_dir),
    )

    assert not ret.success
    assert 'region index' in ret.stderr


def test_find_none(script_runner, regdir):
    """Find with no query produces an error."""
    ret = script_runner.run('admincer', 'find', str(regdir))
    assert not ret.success
    assert 'requires at least one' in ret.stderr


def test_slice(script_runner, slice_source, tmpdir):
    """Test slice sub-command."""
    target = tmpdir.join('output')
    ret = script_runner.run(
        'admincer', 'slice', '--no-empty', '--min-part', '80',
        str(slice_source), str(target)
    )
    assert ret.success
    assert ret.stdout == ''
    assert ret.stderr == ''

    results = idx.reg_index(str(target))
    check_results(results, SLICE_EXPECT['no_empty_80'])


def test_slice_verbose(script_runner, slice_source, tmpdir, check_log):
    """Test slice sub-command."""
    target = tmpdir.join('output')
    ret = script_runner.run(
        'admincer', 'slice', '-v', '--step', '10',
        str(slice_source), str(target)
    )

    assert ret.success
    assert ret.stdout == ''
    check_log(ret.stderr, 'slice-v.log')


def test_convert_one(script_runner, convert_src):
    ret = script_runner.run('admincer', 'convert',
                            str(convert_src.join('14_task11.xml')))

    assert ret.success
    results = idx.reg_index(str(convert_src.join('task11')))
    assert results['1_cut_1.png'] == [(976, 461, 1278, 711, 'textad')]
    assert results['1_cut_0.png'] == [(233, 714, 962, 805, 'bannerad')]


def test_convert_multiple_names(script_runner, convert_src_names):
    convert_src_names.join('whatever.names').write('otherad')
    ret = script_runner.run(
        'admincer', 'convert',
        str(convert_src_names.join('14_task11.xml')),
        str(convert_src_names.join('15_task12.xml'))
    )

    assert ret.success
    results11 = idx.reg_index(str(convert_src_names.join('task11')))
    results12 = idx.reg_index(str(convert_src_names.join('task12')))
    assert results11['1_cut_0.png'] == [(233, 714, 962, 805, 'bannerad')]
    assert results12['5_cut_1.png'] == [(975, 257, 1219, 468, 'popupad')]

    names = 'otherad\nbannerad\ntextad\npopupad'
    assert convert_src_names.join('whatever.names').read() == names
    assert convert_src_names.join('task12', 'class.names').read() == names


def test_convert_and_move(script_runner, convert_src):
    ret = script_runner.run('admincer', 'convert',
                            str(convert_src.join('14_task11.xml')),
                            str(convert_src.join('15_task12.xml')),
                            '-t', str(convert_src.join('converted')), '-m')
    assert ret.success
    results = idx.reg_index(str(convert_src.join('converted')))
    assert results['1_cut_1.png'] == [(976, 461, 1278, 711, 'textad')]
    assert results['1_cut_0.png'] == [(233, 714, 962, 805, 'bannerad')]

    for fn in ['1_cut_0.png', '1_cut_1.png', 'no_ads.png']:
        assert convert_src.join('converted', fn).check(exists=1)
    for fn in ['1_cut_0.png', '1_cut_1.png']:
        assert convert_src.join('task11', fn).check(exists=0)


def test_copy_and_move(script_runner, convert_src):
    """Trying to convert with both 'copy' and 'move' should fail."""
    ret = script_runner.run('admincer', 'convert',
                            str(convert_src.join('15_task12.xml')),
                            '-m', '-c')

    assert not ret.success
    assert 'Choose either "copy" or "move", not both' in ret.stderr
