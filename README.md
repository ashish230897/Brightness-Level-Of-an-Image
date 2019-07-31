# Brightness-Level-Of-an-Image
The following repository calculates the brightness level of an image and outputs a number between 0-10 indicating the brightness of the image.  

## Algorithm Used:
The raw image is first converted to the LAB color space. In this color space, L represents the lightness value,  L = 0 represents the darkest black and L = 100 the brightest white. More about this can be read [here](https://en.wikipedia.org/wiki/CIELAB_color_space).  
The algorithm sees certain portions of the image and takes the maximum L value in those portions. It then outputs the brightness as the average of the maximum L values of these different portions. The algorithm doesn't consider the regions with 0 pixel values since a rather bright image with some dark portions can be assigned a pretty low brightness due to those 0 valued pixels.  

## Code Structure:
* *SampleImages folder* : It contains the sample images whose brightness is to be computed. If a user needs to compute the brightness level, then he/she can insert/delete the images in this same folder. 
* *brightness python file* : This file contains the function for comuputing the brightness level, it forms the core of this repository.
* *main python file* : It is the starting point of the repository. Run this file to get the brightness levels.

## Installation Steps:

Brightness Level requires Python to run.
Install the dependencies and run the *main* python file.

One can first choose to create a virtual environment. The steps for creating and activating the virtual environment are as follows:
```sh
$ conda create --name myenv
$ source activate myenv
```
Later the libraries can be installed as folows:
```sh
$ conda install -c conda-forge opencv
$ pip install matplotlib
```
The python3.7 interpreter can be used further with any ide/jupyter notebook to run the above code then.

