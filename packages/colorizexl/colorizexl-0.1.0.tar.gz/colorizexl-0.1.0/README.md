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

# 