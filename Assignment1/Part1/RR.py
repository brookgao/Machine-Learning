from Part1_config import *

A = robustA(sampX, num)                 # get the A
X = linprogX(D, num, A, sampy).x
Thet = ListToArray(X[0:D]).transpose()

f_pre = Prediction(polyX, Thet)
f_l = ArrayToList(f_pre)

###mean error###
error_avr = MeanSquareError(f_l, polyy_l)
'''
multi_error_list = []
for p in p_list:
    multi_error_avr = MultiErrorAverage_RR(5000, p, sampx_l_multi, sampy_l_multi, polyX, polyy_l, n_s, D)  # multi Error
    multi_error_list.append(multi_error_avr)
print multi_error_list'''
###mean error###

figure = "RR"
title = "RR: Error="+str(error_avr)+", Sample:"+str(percent)+"%"+", K="+str(k)
PlotLines(figure, title, sampx_l, sampy_l, polyx_l, polyy_l,f_l)
