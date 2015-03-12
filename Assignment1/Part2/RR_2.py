__author__ = 'gaobrook'
from Part2_config import *

A = robustA(trainX, n_tr)
X = linprogX(D, n_tr, A, trainy).x
Thet = ListToArray(X[0:D]).transpose()

f_pre = Prediction(testX, Thet)
f_l = ArrayToList_round(f_pre)

error_sq = float(MeanSquareError(f_l, testy))
error_ab = float(MeanAbsoluteError(f_l, testy))
print error_sq
print error_ab


figure = "RR Counting"
title = "RR: Sq Error ="+str(error_sq)+", Ab Error="+str(error_ab)+", D="+str(D)
PlotCounting(figure, title, f_l, testy)