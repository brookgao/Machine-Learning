from Part1_config import *

Thet = LS(sampX, sampy)            # parameters
f_pre = Prediction(polyX, Thet)     # prediction of y
f_l = ArrayToList(f_pre)    # convert array[Y] into list


####average error#####
error_avr = MeanSquareError(f_l, polyy_l)  # average error


'''
p_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]    ### 5000 trials
multi_error_list = []
for p in p_list:
    multi_error_avr = MultiErrorAverage_LS(5000, p, sampx_l_multi, sampy_l_multi, polyX, polyy_l, n_s, D)  # multi Error
    multi_error_list.append(multi_error_avr)
print multi_error_list'''
################


figure = "LS"
title = "LS: Error ="+str(error_avr)+", Sample:"+str(percent)+"%"+", K="+str(k)
PlotLines(figure, title, sampx_l, sampy_l, polyx_l, polyy_l, f_l)
