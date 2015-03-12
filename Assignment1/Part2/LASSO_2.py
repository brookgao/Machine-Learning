__author__ = 'gaobrook'
from Part2_config import *

Lambda = 0.5

H = lassoH(trainX)

Thet_mix = quadprogX(D, H, trainX, trainy, Lambda).x
Thet_plus = ListToArray(Thet_mix[0:D])
Thet_sub = ListToArray(Thet_mix[D:2*D])
Thet = (Thet_plus-Thet_sub).transpose()

f_pre = Prediction(testX, Thet)
f_l = ArrayToList_round(f_pre)

error_sq = float(MeanSquareError(f_l, testy))
error_ab = float(MeanAbsoluteError(f_l, testy))
print error_sq
print error_ab


figure = "LASSO Counting"
title = "LASSO: Sq Error ="+str(error_sq)+", Ab Error="+str(error_ab)+", D="+str(D)
PlotCounting(figure, title, f_l, testy)