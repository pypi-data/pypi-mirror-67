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

"""Indexing images in directories."""

import csv
import functools
import glob
import os

from PIL import Image

IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif']


class Index(dict):
    """Index is a mapping of file names to metadata."""

    def __init__(self, root_path, mapping={}):
        super().__init__(mapping)
        self.root_path = root_path

    @functools.lru_cache(maxsize=32)
    def load_image(self, image_name):
        """Load image from the index."""
        image_path = os.path.join(self.root_path, image_name)
        return Image.open(image_path)

    def add_image(self, image_name, image, metadata=None):
        """Add image into the index."""
        if image_name in self:
            raise KeyError('The index already contains {}'.format(image_name))
        image_path = os.path.join(self.root_path, image_name)
        image.save(image_path)
        self[image_name] = metadata

    def __hash__(self):
        return hash(self.root_path)


class FragmentIndex(Index):
    """Index of a directory with fragments.

    Maps image names/paths to tuples: (width, height).

    """

    def load(self):
        """Load the index from .root_path."""
        for dirpath, dirnames, filenames in os.walk(self.root_path):
            for filename in filenames:
                if any(filename.endswith(ext) for ext in IMAGE_EXTENSIONS):
                    image_path = os.path.join(dirpath, filename)
                    rel_path = os.path.relpath(image_path, self.root_path)
                    image = Image.open(image_path)
                    self[rel_path] = image.size

    def add_image(self, image_name, image):
        """Write image into the index and add it to the index."""
        super().add_image(image_name, image, image.size)


def frag_index(root_path):
    """Return a fragment index of all images under root_path as a dict."""
    ret = FragmentIndex(root_path)
    ret.load()
    return ret


def _clip(x, upper_bound):
    """Return x clipped betweed 0 and upper_bound."""
    if x < 0:
        x = 0
    if x > upper_bound:
        x = upper_bound
    return x


class RegionIndex(Index):
    """Index of a directory with images that have marked regions.

    Maps image names/paths to lists of tuples: (x1, y1, x2, y2, region_type).

    """

    region_types = None  # List of region type names.

    def load(self):
        """Load the index from .root_path."""
        self._load_region_types()
        self._scan_for_images()
        have_csv = self._load_csv_regions()
        have_txt = self._load_yolo_regions()

        if self.region_types is None:
            # Without a provided region types mapping the naming of regions
            # loaded from CSV and TXT files will not be consistent.
            if have_csv and have_txt:
                raise Exception('A .names file is required to allow mixing of '
                                '.csv and .txt regions files.')
            self.region_types = sorted({
                region_type
                for regions in self.values()
                for x1, y1, x2, y2, region_type in regions
            })

        self._clip_regions()

    def add_image(self, image_name, image, regions=[]):
        """Write image into the index root and add regions to the index."""
        super().add_image(image_name, image, regions)

        width, height = image.size
        new_rt = False
        mapped_regions = []

        for x0, y0, x1, y1, rt in regions:
            if rt not in self.region_types:
                self.region_types.append(rt)
                new_rt = True
            t = self.region_types.index(rt)
            x = (x0 + x1) / 2 / width
            y = (y0 + y1) / 2 / height
            w = (x1 - x0) / width
            h = (y1 - y0) / height
            mapped_regions.append((t, x, y, w, h))

        if new_rt:
            self._save_region_types()

        if mapped_regions:
            txt_name = os.path.splitext(image_name)[0] + '.txt'
            txt_path = os.path.join(self.root_path, txt_name)
            with open(txt_path, 'wt', encoding='utf-8') as f:
                for mr in mapped_regions:
                    print(*mr, file=f)

    @functools.lru_cache()
    def _get_image_size(self, image_name):
        """Return image size in pixels as a tuple: (width, height)."""
        image = self.load_image(image_name)
        return image.size

    def _region_types_path(self):
        """Find a .names file inside root_path."""
        names_files = glob.glob(os.path.join(self.root_path, '*.names'))
        if len(names_files) > 1:
            raise Exception('Multiple .names files in {}'
                            .format(self.root_path))
        if len(names_files) == 1:
            return names_files[0]
        return None

    def _load_region_types(self):
        """Load region types from a .names file inside root_path."""
        rt_path = self._region_types_path()
        if rt_path is not None:
            with open(rt_path, 'rt', encoding='utf-8') as f:
                self.region_types = [line.strip() for line in f]

    def _save_region_types(self):
        """Save region types to .names file inside root_path."""
        rt_path = self._region_types_path()
        if rt_path is None:
            rt_path = os.path.join(self.root_path, 'class.names')
        with open(rt_path, 'wt', encoding='utf-8') as f:
            for rt in self.region_types:
                print(rt, file=f)

    def _scan_for_images(self):
        """Find images inside of .root_path and add them to the index."""
        for dirpath, dirnames, filenames in os.walk(self.root_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(file_path, self.root_path)
                if any(filename.endswith(ext) for ext in IMAGE_EXTENSIONS):
                    self[rel_path] = []

    def _clip_regions(self):
        """Clip regions to the image boundaries and remove 0-area ones."""
        for image_name in list(self.keys()):
            width, height = self._get_image_size(image_name)
            clipped_regions = []
            for x1, y1, x2, y2, region_type in self[image_name]:
                x1 = _clip(x1, width)
                x2 = _clip(x2, width)
                y1 = _clip(y1, height)
                y2 = _clip(y2, height)
                if x1 != x2 and y1 != y2:
                    clipped_regions.append((x1, y1, x2, y2, region_type))
            self[image_name] = clipped_regions

    def _load_csv_regions(self):
        """Load regions from any .csv files in root_path."""
        csv_files = glob.glob(os.path.join(self.root_path, '*.csv'))
        for csv_file in csv_files:
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    image_name = row['image']
                    x1, y1, x2, y2 = [
                        int(round(float(row[key])))
                        for key in ['xmin', 'ymin', 'xmax', 'ymax']
                    ]
                    region_type = row['label']
                    self[image_name].append((x1, y1, x2, y2, region_type))
        return csv_files != []

    def _load_yolo_regions(self):
        """Load regions from image_name.txt files."""
        found_some = False

        for image_name in list(self.keys()):
            txt_name = os.path.splitext(image_name)[0] + '.txt'
            txt_path = os.path.join(self.root_path, txt_name)
            if not os.path.exists(txt_path):
                continue

            if self[image_name] != []:
                raise Exception('Regions specified twice for {}'
                                .format(image_name))
            found_some = True

            width, height = self._get_image_size(image_name)
            with open(txt_path, 'rt', encoding='utf-8') as f: 
                for line in f:
                    t, x, y, w, h = line.strip().split()

                    t = int(t)
                    if self.region_types is not None:
                        t = self.region_types[t]
                    else:
                        t = str(t)

                    x, y, w, h = map(float, [x, y, w, h])
                    x1 = int(round((x - w/2) * width))
                    x2 = int(round((x + w/2) * width))
                    y1 = int(round((y - h/2) * height))
                    y2 = int(round((y + h/2) * height))

                    self[image_name].append((x1, y1, x2, y2, t))

        return found_some


def reg_index(root_path, ensure_dir=False):
    """Return the index of marked regions in the images.

    The directory is scanned for image files and the regions map is loaded from
    CSV files in it.

    Parameters
    ----------
    root_path : str
        Path to the directory from which the index is loaded.
    ensure_dir : bool
        If this is True, the root directory will be created if it doesn't
        exist.

    Returns
    -------
    index : RegionIndex
        Index that maps image filenames to lists of tuples that contain
        bounding boxes and region types.

    """
    if ensure_dir:
        os.makedirs(root_path, exist_ok=True)
    ret = RegionIndex(root_path)
    ret.load()
    return ret


def some_index(root_path):
    """Return region index if possible, otherwise fragment index.

    Checks if there are any .csv or .txt files in the directory. If yes,
    attempt RegionIndex, otherwise FragmentIndex.

    """
    csv_files, txt_files = [
        glob.glob(os.path.join(root_path, ext))
        for ext in ['*.csv', '*.txt']
    ]
    if csv_files or txt_files:
        return reg_index(root_path)
    return frag_index(root_path)
