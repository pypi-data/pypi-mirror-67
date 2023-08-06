# ColorizeXL
Python implementation of the following [paper](https://www.cse.huji.ac.il/~yweiss/Colorization/) by Anat Levin, Dani Lischinski, Yair Weiss, puublished in SIGGRAPH04.

We have adapted their technique to make it suitable for large images, by using overlapping patches with annotations.


## Installation:

`pip install colorizexl`


# Usage

## Colorization of Black & White images
Previous to using the package, you have to setup the following:
* original black & white image
* annotation color image (please check details in the paper)


## Recolorization of color images
Previous to using the package, you have to setup the following:
* original color image
* annotation image (please check details in the paper): white where the color stays the same, different colo where yo want to recolorize

## Command line
Call the `colorizexl.py` from command line, to colorize or recolorize images.

`python colorizexl.py --annotated=<path_to_annotated_image>
                      --grayscale=<path_to_image_to_(re)colorize> 
                      --output=<path_to_(re)colorized_image>
                      --recolorize=True/False`

## Python code
```
from colorizexl import ColorizeXL

colorizer = ColorizeXL(
        input_grayscale_name, input_annotation_name, recolorize=False
    )

output = colorizer.colorize(step_size=patch_size, overlap=overlap, n=neighbour)
```

# Customization

From `Python` you have the options to finetune the following parameters:
* `step_size` (default 100), defines the size of the square patches
* `overlap` (default 2), defines the overlap of the patches
* `n` (default 10), defines the radius of the neighbours in a circle for computing the color 

# Package organization

## colorizexl
Contains the ColorizeXL class, the engine behind the (re)colorization.
Its functioning is as follows:
* *__colorize*: will take an `image` and an `annotation` as inputs and will colorize the image; it will return a colorized image
* *colorize*: main entry point in the algorithm, this method will split the initial image in patches and send them to *__colorize*. It will also take care of the overlaps to ensure smooth transition between colorized regions
* *colorize_no_patch*: wrapper for *__colorize* method, this function is the initial implementation of the algorithm, which is slow and will crash for large images

## notebooks
Contains the notebooks used for experimenting:
* *CS445_usage*: example code for colorizing and recolorizing images (example images from the original paper are provided); output of the example images can be seen [here](https://github.com/nfreundlich/colorizexl/blob/master/notebooks/CS445_usage.ipynb)
* *CS445_master*: our inital experiments with colorization
* *CS445_patch_sort*: experiments with intelligent sorting of patches to be recolorized


## tests
Contains the test code used for fine-tuning and evaluating our package.
* *test_hyperparameters*: loops over the hyperparameters (patch size, overlap and neighbours) to compute the MSE (mean squared error), SSIM (structural similarity) and PSNR (peak signal to noise ratio); from these, we have mainly relied on  MSE; it also saves an image for each combination, to allow manual selection of the most pleasing visual effect
* *test_timing*: downscales a large image by a factor of 0.1 to 1.0 (step 0.1) and measures the time needed for computation (please note that the images resulting from downscaling will not necessarily be of a high quality); execution time of our code scales linearly with the number of pixels to recolorize
* *test_timing_no_patch*: similar to *test_timing* but using a one-shot colorization; this original method presents an exponential increase in time per pixels to be colorized