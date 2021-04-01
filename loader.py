import numpy as np
from PIL import Image


class Loader:
    """
    Simple object for loading the images
    """
    def __init__(self, impath_1, impath_2):
        self.image_1 = Image.open(impath_1)
        self.image_2 = Image.open(impath_2)

    def get_images(self):
        """
        Returns the stored images
        :return:
        """
        self.image_1 = np.asarray(self.image_1)
        self.image_2 = np.asarray(self.image_2)

        return self.image_1, self.image_2
