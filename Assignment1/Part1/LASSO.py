__author__ = 'gaobrook'
from Part1_config import *

Lambda = 0.5

H = lassoH(sampX)  #get the H

Thet_mix = quadprogX(D, H, sampX, sampy, Lambda).x
Thet_plus = ListToArray(Thet_mix[0:D])
Thet_sub = ListToArray(Thet_mix[D:2*D])
Thet = (Thet_plus-Thet_sub).transpose()

f_pre = Prediction(polyX, Thet)
f_l = ArrayToList(f_pre)

####average error####
error_avr = MeanSquareError(f_l, polyy_l)

'''
multi_error_list = []
for p in p_list:
    multi_error_avr = MultiErrorAverage_LASSO(5000, p, sampx_l_multi, sampy_l_multi, polyX, polyy_l, n_s, D)  # multi Error
    multi_error_list.append(multi_error_avr)
print multi_error_list'''
######average error####


figure = "LASSO"
title = "LASSO: Lambda="+str(Lambda)+", Error="+str(error_avr)+", Sample:"+str(percent)+"%"+", K="+str(k)
PlotLines(figure, title, sampx_l, sampy_l, polyx_l, polyy_l, f_l)
