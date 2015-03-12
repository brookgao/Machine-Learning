__author__ = 'gaobrook'
from scipy import *
import matplotlib.pyplot as plt
from numpy import *
from numpy.linalg import *
from random import *


def Txt_to_Mix(file, row , colum):
    i = 0
    Mix = ones((row, colum))
    for lines in file:
        Mix[i] = array([lines.split()], dtype=float)
        i += 1
    return Mix

def ArrayToList_round(array):      #### number of persons
    list = []
    for i in range(len(array)):
        list.append(round(array[i]))
    return list

def MeanAbsoluteError(f_l, testy):        # mean-absolute error
    sum = 0
    n = len(testy)
    for i in range(n):
        error = f_l[i]-testy[i]
        sum += (abs(error))
    avr = sum/n
    return avr

def PlotCounting(figure, title, f_l, testy, f_sub=None, f_plus=None):
    x_l =range(0, 600)
    plt.figure(figure+' Log')
    plt.title(title)
    if(figure == 'BR Counting'):
        plt.plot(x_l, f_sub, "b-", label="Prediction Mju-(sigma**1/2)")
        plt.plot(x_l, f_plus, "b-", label="Prediction Mju+(sigma**1/2)")
    plt.plot(x_l, f_l, "r-", label="Prediction")
    plt.plot(x_l, testy, "g-", label="True output")
    plt.legend(loc=1)
   # plt.savefig('/Users/gaobrook/Desktop/Regression/part2/b/e/'+figure+'.jpg', dpi=200)
    plt.show()


