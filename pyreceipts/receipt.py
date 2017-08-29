import os
from PIL import Image
import pytesseract
import tempfile


class Receipt:
    MIN_WIDTH = 900

    def __init__(self, file_name):
        self._validate_image(file_name)

        self.file_name = file_name
        self.tmp_file_path = '%s_tmp.jpg' % file_name
        self.original_file = Image.open(self.file_name)

        self._enlarge_image(self.original_file)
        self.image = Image.open(self.tmp_file_path)

    def _save_to_tmp(self, img):
        img.save(self.tmp_file_path, dpi=(600, 600))
        return img

    def _validate_image(self, file_name):
        if not os.path.exists(file_name):
            raise ValueError('This file does not exists!')

    def _enlarge_image(self, img):
        # File should have at least 900px width to be read properly
        if img.size[0] < self.MIN_WIDTH:
            width_percent = (self.MIN_WIDTH/float(img.size[0]))
            height = int(float(img.size[1])*float(width_percent))
            img = img.resize((self.MIN_WIDTH, height), Image.ANTIALIAS)
        self._save_to_tmp(img)
        return img

    def read(self):
        return pytesseract.image_to_string(self.image)

    def delete_tmp_file(self):
        os.remove(self.tmp_file_path)
