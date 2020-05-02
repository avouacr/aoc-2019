
import numpy as np
from matplotlib.pyplot import imshow

def img_to_array(input, W, H):
    n_pixels = W * H
    n_layers = len(input) // (W * H)
    pixel_values = np.array([int(n) for n in input])
    layers = np.split(pixel_values, n_layers)
    layers = [x.reshape((H, W)) for x in layers]
    image_array = np.stack(layers, axis=2)
    return image_array

def check_corruption(img_array):
    H, W, n_layers = img_array.shape
    count_nonzeros = np.count_nonzero(img_array, (0, 1))
    layer_min_0 = np.argmax(count_nonzeros)
    n_one = (img_array[:,:,layer_min_0] == 1).sum()
    n_two = (img_array[:, :, layer_min_0] == 2).sum()
    return n_one * n_two

def decode_img(img_array):
    H, W, n_layers = img_array.shape
    img_out = np.zeros((H, W))
    for i in range(H):
        for j in range(W):
            channel = img_array[i,j,:]
            color = channel[np.argmax(channel != 2)]
            img_out[i,j] = color
    return img_out


# input = '123456789012'
# input = '0222112222120000'

with open('day8/input', 'r') as f:
    input = f.read().splitlines()
input = input[0]

img_array = img_to_array(input, 25, 6)

# Part 1
check_corruption(img_array)

# Part 2
decoded = decode_img(img_array)
imshow(decoded)