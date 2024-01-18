# Image Comparison Tool

## Overview
This Python script provides a straightforward utility to check whether two images are exactly the same. It compares images pixel by pixel to determine if they are identical.

## Requirements
- Python 3.x
- Pillow library

## Installation
Before running the script, ensure you have Python installed on your system. You can download Python from [the official Python website](https://www.python.org/downloads/).

Once Python is installed, you will need the Pillow library, which is a fork of PIL (Python Imaging Library). Install it using pip:

```bash
pip install Pillow
```

## Usage
To use the script, simply place your image files in a desired directory and modify the script to include the correct file paths.

Example:
```python
image_path1 = 'path/to/your/first/image.jpg'
image_path2 = 'path/to/your/second/image.jpg'

if images_are_same(image_path1, image_path2):
    print("Images are the same.")
else:
    print("Images are different.")
```

## Functionality
The script works by comparing two images in the following manner:
1. Checks if both images have the same dimensions.
2. Compares each pixel of both images.

If both the dimensions and all pixels are identical, the script concludes the images are the same.

## Limitations
- The script only works for images that are expected to be identical in every aspect (size, format, pixel data).
- It is not suitable for comparing images with minor variations such as compression differences or color variations.
- The script does not handle cases where images are visually similar but not pixel-perfect identical.


