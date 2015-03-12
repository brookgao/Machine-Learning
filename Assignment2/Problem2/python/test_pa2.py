# CS5487 demo script for Programming Assignment 2
#
# The script has been tested with python 2.7.6
#
# It requires the following modules:
#   numpy 1.8.1
#   matplotlib v1.3.1
#   scipy 0.14.0
#   Image (python image library)

import pa2
import numpy as np
import pylab as pl
import scipy.io as sio
from PIL import Image
from Assignment2.Problem1.K_means import *
from Assignment2.Problem1.EM import *
from Assignment2.Problem1.Mean_shift import *
from Assignment2.Problem1.P1_function import *

#import Image
def demo():
    import scipy.cluster.vq as vq

    ## load and show image
    img = Image.open('../images/12003.jpg')
    pl.subplot(1, 3, 1)
    pl.imshow(img)
    
    ## extract features from image (step size = 7)
    X, L = pa2.getfeatures(img, 7)


    ## Call kmeans function in scipy.  You need to write this yourself!
   # C,Y = vq.kmeans2(vq.whiten(X.T), 2, iter=1000, minit='random')

    d = 4
    K = 4
    N = X.shape[1]
    Mju = RandomMju(150, 155, K, d)
    ##########Kmeans##########
    #Y = Clustering_Kmeans(Mju, X, K, N, d, 1000, 0.000000000001)


     ##########EM#########
    #d = 4
    #K = 2
    #SIGMA = RandomSIGMA(100, 110, K, d)

    #Pi = [0.1, 0.1, 0.05, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05, 0.2]
    #Y = Clustering_EM(Mju, SIGMA, Pi, X, K, d, X.shape[1], 800, 0.00000000000001)
     ###################


    #####Meanshift####
    h = 45

    maxRound = 30
    limitation = 0.00001
    cluster_gap = 8
    X_peak = Peak_MeanShift(X, d, N, h, maxRound, limitation)
    cluster = Clustering_MeanShift(X, X_peak, N, d, cluster_gap)
    Y = cluster[1]
    ##########################



    # Use matlab 1-index labeling

    # make segmentation image from labels
    segm = pa2.labels2seg(Y, L)
    pl.subplot(1, 3, 2)
    pl.imshow(segm)
    
    # color the segmentation image
    csegm = pa2.colorsegms(segm, img)
    picname ="seastar"
    title = "Menshift, h="+str(h)
    pl.title(title)
    pl.subplot(1, 3, 3)
    pl.imshow(csegm)
    pl.savefig('/Users/gaobrook/Desktop/Clustering/problem2/'+title+'_'+picname+'.png', dpi=200)
    pl.show()

def main():
    demo()
if __name__ == '__main__':
    main()
