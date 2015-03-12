__author__ = 'gaobrook'
import matplotlib.pyplot as plt
from numpy import *
from numpy.linalg import *
import math as math
from random import *

def TextConvertToMix(lines, row, colum):
    i = 0
    Mix = zeros((row, colum), dtype=float)
    for lines in lines:
        Mix[i] = array([lines.split()], dtype=float)
        i += 1
    return Mix

def ListToArray(list):               # convert list to array
    arr = array([list], dtype=float)
    return arr

def RandomMju(start, end, K, d):        #get random Mju
    if(d ==2):
        for i in range(K):
            mju1 = uniform(start, end)
            mju2 = uniform(start, end)
            if(i == 0):
                Mju = array([[[mju1], [mju2]]])
            else:
                tmp = array([[[mju1], [mju2]]])
                Mju = vstack((Mju, tmp))
    elif(d == 4):
        for i in range(K):
            mju1 = uniform(start, end)
            mju2 = uniform(start, end)
            mju3 = uniform(start, end)
            mju4 = uniform(start, end)
            if(i == 0):
                Mju = array([[[mju1], [mju2], [mju3], [mju4]]])
            else:
                tmp = array([[[mju1], [mju2], [mju3], [mju4]]])
                Mju = vstack((Mju, tmp))
    return Mju

def RandomSIGMA(start, end, K, d):       #get random SIGMA

    for i in range(K):
        if(i == 0):
            SIGMA = uniform(start, end)*array([eye(d)])
        else:
            tmp = uniform(start, end)*array([eye(d)])
            SIGMA = vstack((SIGMA, tmp))
    return SIGMA

def MultiGaussian(X, Mju, SIGMA, d):         #value of MultiGaussian
    part1 = 1/(pow(2*math.pi, d/2.0)*pow(det(SIGMA), 1/2.0))
   # print "part1 =", part1

    part2 = (-1/2.0)*dot(dot(transpose(X - Mju), inv(SIGMA)), X - Mju)
   # print "part2 =", part2

    part3 = pow(math.e, part2)
   # print "part3 =", part3

    res = part1*part3
    return float(res)



def PlotCluster(figure, title, X, Y, N):
    X = transpose(X)

    k1 = zeros((2, 1))
    k2 = zeros((2, 1))
    k3 = zeros((2, 1))
    k4 = zeros((2, 1))
    for i in range(N):
        x = transpose(array([X[i]]))
        k_choose = int(Y[0][i])
        if(k_choose == 1):
            k1 = hstack((k1, x))
        elif(k_choose == 2):
            k2 = hstack((k2, x))
        elif(k_choose == 3):
            k3 = hstack((k3, x))
        elif(k_choose == 4):
            k4 = hstack((k4, x))

    plt.figure(figure)
    plt.title(title)
    plt.plot(k1[0][1:], k1[1][1:], "go", label="k1")
    plt.plot(k2[0][1:], k2[1][1:], "bo", label="k2")
    plt.plot(k3[0][1:], k3[1][1:], "ro", label="k3")
    plt.plot(k4[0][1:], k4[1][1:], "co", label="k4")
    plt.axis([-15, 15, -15, 15])
    plt.legend(loc=3)
    plt.grid(True)
    plt.show()