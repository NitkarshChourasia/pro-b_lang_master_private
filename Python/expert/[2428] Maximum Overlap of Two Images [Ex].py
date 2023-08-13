"""
####  Maximum Overlap of Two Images  ####

The function is given two equal size matrices of integers. Each cell holds a pixel: 1 represents a black pixel, 0 represents a white pixel. One of the images can be shifted in any two directions (up, down, left, right) relative to another image by any number of cells, e.g. (2 up, 1 right) or (1 down, 0 left). Determine the maxim possible overlap of black pixels of the two images.


[Examples]

___
max_overlap([[1]], [[1]]) ➞ 1
# Each image has only one pixel.

max_overlap([[0]], [[0]]) ➞ 0
# No pixels in any image

max_overlap([[1, 1, 0],
             [0, 1, 0]],
            [[0, 1, 1],
             [0, 0, 1]]) ➞ 3
# The first image can be shifted to the right by 1 to get 3-pixel overlap.

max_overlap([[0, 1, 0],
             [1, 1, 0]],
            [[0, 1, 1],
             [0, 0, 1]]) ➞ 2
# The first image can be shifted 1-right, 1-up to get 2-pixel overlap.

max_overlap([[1, 1],
             [1, 1]],
            [[0, 0],
             [1, 1]]) ➞ 2
# Without any shift a 2-pixel overlap is achieved and it cannot be larger.
_____



[Notes]

N/A


[algorithms] [arrays] [conditions] [data_structures] 



-------------------------------------------------------------------
[Resources]
_________
Fast Fourier Transform
https://en.wikipedia.org/wiki/Fast_Fourier_transform
Iis an algorithm that computes the discrete Fourier transform (DFT) of a sequence, or its inverse (IDFT). Fourier analysis converts a signal from its original domain (o …
_________
_________
Discrete Fourier transform
https://en.wikipedia.org/wiki/Discrete_Fourier_transform
In mathematics, the discrete Fourier transform (DFT) converts a finite sequence of equally-spaced samples of a function into a same-length sequence of equally-spaced sa …
_________

"""
#Your code should go here:

