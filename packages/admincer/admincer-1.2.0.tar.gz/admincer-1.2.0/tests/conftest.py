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

"""Common fixtures."""

from PIL import Image
import pytest
import py


class Colors:
    """Colors for composing images and checking output images."""
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    ORANGE = (255, 165, 0)
    BLUE = (0, 0, 255)
    PINK = (255, 128, 128)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)


def make_image(path, width, height, color=Colors.WHITE):
    """Make a dummy image for testing."""
    Image.new('RGB', (width, height), color).save(str(path))


@pytest.fixture()
def logs_dir():
    """Directory with expected logs."""
    return py.path.local(__file__).dirpath().join('data', 'logs')


@pytest.fixture()
def fragdir(tmpdir):
    """Directory with some image fragments."""
    ret = tmpdir.mkdir('fragdir')
    make_image(ret.join('red.gif'), 10, 20, Colors.RED)
    make_image(ret.join('green.png'), 30, 40, Colors.GREEN)
    make_image(ret.mkdir('subdir').join('orange.jpg'), 50, 60, Colors.ORANGE)
    ret.join('other.sh').write('# random unrelated file')
    return ret


@pytest.fixture()
def regdir(tmpdir):
    """Directory with some images with marked regions."""
    ret = tmpdir.mkdir('regdir')
    # White square with 2 regions (see below for regions).
    make_image(ret.join('white2.png'), 100, 100, Colors.WHITE)
    # Blue rectangle with 3 regions.
    make_image(ret.join('blue3.png'), 200, 100, Colors.BLUE)
    # Black square with no regions.
    make_image(ret.join('black.gif'), 100, 100, Colors.BLACK)
    ret.join('index.csv').write('\n'.join([
        # Some rows have text in quotes while others don't. We should be
        # compatible with both styles.
        '"image","xmin","ymin","xmax","ymax","label"',
        '"white2.png",10.34,20.12,19.79,39.9,"r1"',
        'white2.png,50,50,80,90,r2',
        'blue3.png,10,10,20,20,r1',
        'blue3.png,40,10,50,20,r1',
        'blue3.png,10,30,60,90,r3',
    ]))
    return ret


@pytest.fixture()
def regdir_var(tmpdir, regdir):
    """Directory with images and regions in different formats."""
    ret = tmpdir.join('regdir_var')
    regdir.copy(ret)
    ret.join('index.csv').write('\n'.join([
        'image,xmin,ymin,xmax,ymax,label',
        'black.gif,10,10,20,20,r1',
    ]))
    ret.join('region.names').write('\n'.join(['r1', 'r2', 'r3', '']))
    ret.join('white2.txt').write('\n'.join([
        '0 0.05 0.2 0.2 0.5',  # Should be clipped from top and left.
        '1 0.85 0.9 0.4 0.4',  # Should be clipped from bottom and right.
        '',
    ]))
    ret.join('blue3.txt').write('\n'.join([
        '0 0.075 0.15 0.05 0.1',
        '1 0.225 0.15 0.05 0.1',
        '2 0.175 0.6 0.25 0.6',
    ]))
    return ret


@pytest.fixture()
def regdir_with_clipping(tmpdir):
    """Directory with some images with marked regions."""
    ret = tmpdir.mkdir('regdir_with_clipping')
    # Red square with 3 regions, all in need of clipping
    make_image(ret.join('red3.png'), 100, 90, Colors.BLACK)
    ret.join('index.csv').write('\n'.join([
        # Some rows have text in quotes while others don't. We should be
        # compatible with both styles.
        '"image","xmin","ymin","xmax","ymax","label"',
        'red3.png,-10,80,20,120,r1',
        'red3.png,90,-20,130,20,r1',
        'red3.png,0,20,0,50,r1',
        'red3.png,20,0,30,0,r1',
    ]))
    return ret


@pytest.fixture()
def regdir_pandas(tmpdir):
    """Directory with images and regions in pandas format."""
    ret = tmpdir.mkdir('regdir_pandas')
    make_image(ret.join('black.gif'), 100, 100, Colors.BLACK)
    make_image(ret.join('blue3.png'), 200, 100, Colors.BLUE)
    make_image(ret.join('white2.png'), 100, 100, Colors.WHITE)
    ret.join('regions.csv').write('\n'.join([
        ',image,xmin,ymin,xmax,ymax,label',
        '0,black.gif,10,10,20,20,r1',
        '1,blue3.png,10,10,20,20,r2',
        '2,white2.png,50,50,80,90,r3',
    ]))
    return ret


def _char_to_color(c):
    """Convert character to an RGB color."""
    code = ord(c)
    r = (code & 0b11) * 64
    g = ((code >> 2) & 0b11) * 64
    b = ((code >> 4) & 0b111) * 32
    return (r, g, b)


def _color_to_char(color):
    """Convert RGB color to a character."""
    r, g, b = color
    low = int(round(r / 64))
    mid = int(round(g / 64)) * 4
    hi = int(round(b / 32)) * 16
    code = low + mid + hi
    return chr(code)


def chars_to_image(chars, cell_size=8, width=4, height=4):
    """Make an image based on a string of characters.

    Parameters
    ----------
    chars : str
        Characters that define the colors of cells.
    cell_size : int
        Height and width of each cell (which will be colored the same).
    width : int
        Width of the image (in cells).
    height : int
        Height of the image (in cells).

    Returns
    -------
    img : PIL.Image
        Resulting image.

    """
    colors = [_char_to_color(c) for c in chars]
    img = Image.new('RGB', (cell_size * width, cell_size * height))
    img.putdata([
        colors[row * width + col]
        for row in range(height)
        for y in range(cell_size)
        for col in range(width)
        for x in range(cell_size)
    ])
    return img


def image_to_chars(image, cell_size=8, width=4, height=4):
    """Convert image produced by chars_to_image back to sting of characters.

    Parameters
    ----------
    image : PIL.Image
        Image to convert.
    cell_size : int
        Height and width of each cell (which will be colored the same).
    width : int
        Width of the image (in cells).
    height : int
        Height of the image (in cells).

    Returns
    -------
    chars : str
        The characters for the image.

    """
    assert image.size == (cell_size * width, cell_size * height)
    offset = cell_size // 2
    return ''.join(
        _color_to_char(image.getpixel((col * cell_size + offset,
                                       row * cell_size + offset)))
        for row in range(height)
        for col in range(width)
    )


# Characters to make images from.
STRINGS = [
    'just some random',
    'chars here to ma',
    'e fragments from',
    'f23sj09xczvnm,we',
]


def _make_needles():
    """Make 4 distinct 32x32 images to use as pieces of big images."""
    return [chars_to_image(chars) for chars in STRINGS]


def _make_haystack(needles):
    """Make 4 images that contain some of the needles."""
    needle_placements = [
        [0, 1, 2],
        [2, 3],
        [0, 2],
        [1, 3],
    ]
    filler = chars_to_image('for the bckground')

    ret = []
    for np in needle_placements:
        img = Image.new('RGB', (100, 200))
        for x in [0, 30, 60, 80]:
            for y in [0, 30, 60, 90, 120, 150, 170]:
                img.paste(filler, (x, y, x + 32, y + 32))
        for i, n in enumerate(np):
            needle = needles[n]
            img.paste(needle, (i * 20, i * 50, i * 20 + 32, i * 50 + 32))
        ret.append(img)

    return ret


@pytest.fixture(scope='session')
def fragfind_dir(tmpdir_factory):
    """Directory that contains files for testing the fragment search."""
    ret = tmpdir_factory.mktemp('fragdir')
    needles_dir = ret.mkdir('needles')
    haystack_dir = ret.mkdir('haystack')

    needles = _make_needles()

    for i, needle in enumerate(needles):
        path = needles_dir.join('{}.png'.format(i))
        print('saving to {}'.format(path))
        needle.save(str(path))
    
    haystack = _make_haystack(needles)

    for i, img in enumerate(haystack):
        # Save these ones as JPG to test inexact matching.
        path = haystack_dir.join('{}.jpg'.format(i))
        img.save(str(path))

    haystack_dir.join('regions.csv').write('\n'.join([
        'image,xmin,ymin,xmax,ymax,label',
        '0.jpg,0,0,10,10,r1',
        '1.jpg,0,0,10,10,r2',
        '2.jpg,0,0,17,10,r1',
        '3.jpg,0,0,10,10,r1',
    ]))

    return ret


SLICE_STRINGS = [
    '123456789',
    'abcdefghi',
    'jklmnopqrstu',
    'ABCDEFGHIJKLMNOPQRSTUVWX',
]


@pytest.fixture(scope='session')
def slice_source(tmpdir_factory):
    """Source directory for tests of slicing functionality."""
    ret = tmpdir_factory.mktemp('slice_source')

    for i in range(len(SLICE_STRINGS)):
        chars = SLICE_STRINGS[i]
        image = chars_to_image(chars, 10, 3, len(chars) // 3)
        image.save(str(ret.join('{}.png'.format(i))))

    ret.join('regions.csv').write('\n'.join([
        'image,xmin,ymin,xmax,ymax,label',
        '0.png,0,0,10,10,r1',
        '0.png,20,10,30,30,r2',
        '2.png,0,0,10,10,r1',
        '2.png,20,0,30,20,r3',
        '2.png,20,30,30,40,r1',
        '3.png,20,10,30,30,r1',
        '3.png,20,60,30,80,r2',
    ]))

    return ret


@pytest.fixture()
def cvat_dir():
    """Directory with CVAT-style annotation files."""
    return py.path.local(__file__).dirpath().join('data', 'cvat_xmls')


@pytest.fixture()
def convert_src(tmpdir_factory, cvat_dir):
    """Source directory for tests of converting functionality."""
    ret = tmpdir_factory.mktemp('convert_source')
    task11_images = ret.mkdir('task11')
    task12_images = ret.mkdir('task12')

    cvat_dir.join('14_task11.xml').copy(ret.join('14_task11.xml'))
    cvat_dir.join('15_task12.xml').copy(ret.join('15_task12.xml'))

    make_image(task11_images.join('1_cut_0.png'), 1351, 1351, Colors.WHITE)
    make_image(task11_images.join('1_cut_1.png'), 1351, 1351, Colors.BLUE)
    make_image(task11_images.join('no_ads.png'), 1351, 1351, Colors.RED)
    make_image(task12_images.join('5_cut_1.png'), 1351, 1351, Colors.BLACK)
    make_image(task12_images.join('2_cut_0.png'), 1351, 1351, Colors.RED)

    return ret


@pytest.fixture()
def convert_src_names(tmpdir_factory, cvat_dir):
    """Directory with CVAT annotations and .names files."""
    ret = tmpdir_factory.mktemp('convert_source')
    task11_images = ret.mkdir('task11')
    task12_images = ret.mkdir('task12')

    task11_images.join('class.names').write('bannerad\ntextad\n')
    task12_images.join('class.names').write('textad\nbannerad\npopupad')

    cvat_dir.join('14_task11.xml').copy(ret.join('14_task11.xml'))
    cvat_dir.join('15_task12.xml').copy(ret.join('15_task12.xml'))

    make_image(task11_images.join('1_cut_0.png'), 1351, 1351, Colors.WHITE)
    make_image(task11_images.join('1_cut_1.png'), 1351, 1351, Colors.BLUE)
    make_image(task12_images.join('5_cut_1.png'), 1351, 1351, Colors.BLACK)
    make_image(task12_images.join('2_cut_0.png'), 1351, 1351, Colors.RED)

    return ret


@pytest.fixture()
def bad_convert_src(tmpdir_factory, cvat_dir):
    """Source directory for tests of converting functionality."""
    ret = tmpdir_factory.mktemp('convert_source')
    task11_images = ret.mkdir('task11')

    cvat_dir.join('14_task11.xml').copy(ret.join('14_task11.xml'))
    make_image(task11_images.join('1_cut_0.png'), 1351, 1351, Colors.WHITE)

    return ret
