__author__ = 'gaobrook'

from Part2_config import *

Lambda = 0.4

Thet = RLS(trainX, trainy, Lambda, D)
f_pre = Prediction(testX, Thet)
f_l = ArrayToList_round(f_pre)

error_sq = float(MeanSquareError(f_l, testy))
error_ab = float(MeanAbsoluteError(f_l, testy))
print error_sq
print error_ab

figure = "RLS Counting"
title = "RLS: Sq Error ="+str(error_sq)+", Ab Error="+str(error_ab)+", D="+str(D)
PlotCounting(figure, title, f_l, testy)