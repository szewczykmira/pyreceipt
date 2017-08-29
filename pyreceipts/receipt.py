import os
from PIL import Image
import pytesseract
import tempfile


class Receipt:
    MIN_WIDTH = 900

    def __init__(self, file_name):
        self.file_name = file_name
        self._validate_data()
        self.image = self._process()

    @property
    def tmp_file_path(self):
        return self.file_name + '_tmp.jpg'

    def _validate_data(self):
        if not os.path.exists(self.file_name):
            raise ValueError('This file does not exists!')

    def _process(self):
        # File should have at least 900px width to be read properly
        img = Image.open(self.file_name)
        if img.size[0] < self.MIN_WIDTH:
            img = self._enlarge_image(img)
        img.save(self.tmp_file_path)
        return Image.open(self.tmp_file_path)

    def _enlarge_image(self, img):
        width_percent = (self.MIN_WIDTH/float(img.size[0]))
        height = int(float(img.size[1])*float(width_percent))
        return img.resize((self.MIN_WIDTH, height), Image.ANTIALIAS)

    def read(self):
        return pytesseract.image_to_string(self.image)

    def delete_tmp_file(self):
        os.remove(self.tmp_file_path)
