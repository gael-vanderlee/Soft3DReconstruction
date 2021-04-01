import numpy as np
from scipy.ndimage.interpolation import shift
from tqdm import trange
import matplotlib.pyplot as plt
from config import output_folder


class DepthEstimator:
    """
    Uses Stero matching and guided image filtering to estimate depth
    """
    def __init__(self, im1, im2, imname):
        self.im1 = im1 / 255
        self.im2 = im2 / 255
        self.imname = imname
        self.shifted_im2 = None
        self.depth_map = None

        self.d = 26
        self.shift_amount = 1
        self.Tc = 0.028
        self.Tg = 0.008
        self.alpha = 0.9
        self.r = 9
        self.epsilon = 100
        self.abs_diffs = np.zeros(im1.shape[:3] + (self.d,))
        self.gradients = np.zeros(im1.shape[:3] + (self.d,))
        self.costs = np.zeros(im1.shape[:3] + (self.d,))
        self.c_prime = np.zeros(im1.shape[:2] + (self.d,))

    def compute_depth(self):
        """
        Core of the objects, runs through the member functions in order
        :return:
        """
        for d in trange(self.d, desc=f"Computing depth maps for {self.imname} "):
            self.shifted_im2 = shift(self.im2, shift=(0, -d * self.shift_amount, 0), order=0)
            self.abs_diffs[:, :, :, d] = self.absolute_difference()
            self.gradients[:, :, :, d] = self.compute_gradients()
            self.costs[:, :, :, d] = self.compute_costs(d)
            self.c_prime[:, :, d] = self.compute_cprime(d)
        self.depth_map = np.min(self.c_prime, axis=2)
        print("Done!")
        self.show()
        return self.depth_map

    def absolute_difference(self):
        """
        Computes the absolute difference between im1 and shifted_im2, summing across colors
        """
        return np.repeat(
            np.expand_dims(
                np.sum(
                    np.abs(self.im1 - self.shifted_im2), axis=2),
                axis=2),
            3, 2)

    def compute_gradients(self):
        """
        Computes the gradients for im1 and shifted_im2
        :return: the absolute value of the pairwise difference of the gradients
        """
        gradients_im1 = np.gradient(self.im1, axis=1)
        gradients_im2 = np.gradient(self.shifted_im2, axis=1)
        return np.abs(gradients_im1 - gradients_im2)

    def compute_costs(self, d):
        """
        Computes the cost of a certain depth map
        :param d: depth map index
        :return: the cost matrix associated with the depth map
        """
        return self.alpha * np.minimum(np.full(self.im1.shape[:3], self.Tc), self.abs_diffs[:, :, :, d]) + \
               (1 - self.alpha) * np.minimum(np.full(self.im1.shape[:3], self.Tg), self.gradients[:, :, :, d])

    def compute_cprime(self, d):
        """
        Computes the filtered cost value
        :param d: depth map index
        :return: filtered cost map
        """
        def filter(img, radius):
            rows, cols = img.shape
            image_distance = np.zeros(img.shape)

            image_sum = np.cumsum(img, 0)
            image_distance[0: radius + 1, :] = image_sum[radius: 2 * radius + 1, :]
            image_distance[radius + 1: rows - radius, :] = image_sum[2 * radius + 1: rows, :] - \
                                                           image_sum[0: rows - 2 * radius - 1, :]
            image_distance[rows - radius: rows, :] = np.tile(image_sum[rows - 1, :], [radius, 1]) - \
                                                     image_sum[rows - 2 * radius - 1: rows - radius - 1, :]

            image_sum = np.cumsum(image_distance, 1)
            image_distance[:, 0: radius + 1] = image_sum[:, radius: 2 * radius + 1]
            image_distance[:, radius + 1: cols - radius] = image_sum[:, 2 * radius + 1: cols] - \
                                                           image_sum[:, 0: cols - 2 * radius - 1]
            image_distance[:, cols - radius: cols] = np.tile(image_sum[:, cols - 1], [radius, 1]).T - \
                                                     image_sum[:, cols - 2 * radius - 1: cols - radius - 1]

            return image_distance

        cost = self.costs[:, :, :, d].mean(axis=2)
        guide = self.im1.mean(axis=2)

        N = filter(np.ones([guide.shape[0], guide.shape[1]]), self.r)
        mean_guide = filter(guide, self.r) / N
        mean_cost = filter(cost, self.r) / N
        mean_both = filter(guide * cost, self.r) / N

        varI = filter(guide * guide, self.r) / N - mean_guide * mean_guide

        a = mean_both - mean_guide * mean_cost / (varI + self.epsilon)
        b = mean_cost - a * mean_guide

        meanA = filter(a, self.r) / N
        meanB = filter(b, self.r) / N
        return meanA * guide + meanB

    def show_arr(self, arr, title):
        """
        Helper function to avoid duplicated code
        :param arr: numpy 2d or 3d array
        :param title: title for saving and displaying
        """
        plt.imshow((arr / arr.max())-arr.min())
        plt.title(title)
        fname = str(output_folder / title.replace(" ", "_"))
        plt.savefig(fname)
        plt.show()

    def show(self):
        """
        Displays insternal states
        """
        # for im in [self.im1, self.im2]:
        #     image = Image.fromarray(im)
        #     image.show()
        for d in [0]:
            self.show_arr(self.abs_diffs[:, :, :, d], f"{self.imname} Absolute difference {d}")
            self.show_arr(self.gradients[:, :, :, d], f"{self.imname} Gradient {d}")
            self.show_arr(self.costs[:, :, :, d], f"{self.imname} Cost {d}")
            self.show_arr(self.c_prime[:, :, d], f"{self.imname} C' {d}")
        self.show_arr(self.depth_map, f"{self.imname} Depth map")
