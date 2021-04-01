from loader import Loader
from config import input_folder, image_1_path, image_2_path
from depth_estimation import DepthEstimator


def recontruct():
    """
    Runs through the 3D recontruction pipeline
    :return:
    """

    # Manual file paths
    if image_1_path is not None and image_2_path is not None:
        loader = Loader(image_1_path, image_2_path)
        im1, im2 = loader.get_images()
        estimator = DepthEstimator(im1, im2, image_1_path.stem[:-1])
        estimator.compute_depth()
        return

    # Automatically finds images in inputs/
    seen_images = set()
    for imfile in input_folder.iterdir():
        imname = imfile.stem[:-1]
        if imname in seen_images:
            im1_path = input_folder / (imname + "1.png")
            im2_path = input_folder / (imname + "2.png")
            loader = Loader(im1_path, im2_path)
            im1, im2 = loader.get_images()
            estimator = DepthEstimator(im1, im2, imname)
            estimator.compute_depth()
        else:
            seen_images.add(imname)

    # TODO add soft 3D recontruction from depth maps


if __name__ == '__main__':
    recontruct()

