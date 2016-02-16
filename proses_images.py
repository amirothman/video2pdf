import os
import numpy as np
from skimage import data

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    
    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

directory_path = "image_temp"
errors = []
filenames = []
for root, dirs, files in os.walk(directory_path):
    _buffer = None
    for idx, _file in enumerate(sorted(files)):
        if _buffer is not None:
            image = data.imread("/".join([directory_path,_file]))
            # print(image.shape,_buffer.shape)
            # do processing
            errors.append(mse(image,_buffer))
            filenames.append(_file)
            # print(ssim(image,_buffer))
            _buffer = image
        else:
            _buffer = data.imread("/".join([directory_path,_file]))

top_distance = np.percentile(errors,95)

selected_files = [filenames[errors.index(distance)] for distance in errors if distance > top_distance]

for _filename in selected_files:
    print("cp image_temp/{0} selected_images".format(_filename))