__author__ = 'gaobrook'
from Part2_config import *

Alpha = 5
sigma = 5

SIGMA = BR_SIGMA(trainX, Alpha, sigma, D)        # variance
Mju = BR_Mju(trainX, sigma, SIGMA, trainy)        # mean

f_arr = Prediction(testX, Mju)                   # prediction of mean [array]
PreSIGMA = GaussianPreSIGMA(testX, SIGMA, n_te, D)   # prediction of variance [list]
f_l = ArrayToList(f_arr)                    # mean [list]

f_plus = []
f_sub = []
for i in range(len(f_l)):
    f_plus.append(f_l[i]+PreSIGMA[i])
    f_sub.append(f_l[i]-PreSIGMA[i])

error_sq = float(MeanSquareError(f_l, testy))
error_ab = float(MeanAbsoluteError(f_l, testy))
print error_sq
print error_ab


figure = "BR Counting"
title = "BR: Sq Error ="+str(error_sq)+", Ab Error="+str(error_ab)+", D="+str(D)
PlotCounting(figure, title, f_l, testy, f_sub, f_plus)