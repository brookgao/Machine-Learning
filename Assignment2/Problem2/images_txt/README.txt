This archive contains the text versions of image features.

filename_X.txt = matrix of feature vectors for image.
filename_L.txt = some information about the image.

The features are extracted using the following MATLAB command:
  [X, L] = getfeatures(img, 7);


** Important Note **
The number format is 16-digit double, and tab delimited.
The matrices are transposed in the text file.  
That is, each row in the text file corresponds to a column of a matrix.

So if the file contains:

1 2 3 4
5 6 7 8

Then this is actually a 4 x 2 matrix:
  1 5
  2 6
  3 7 
  4 8

