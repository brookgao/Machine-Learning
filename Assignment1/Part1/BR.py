from Part1_config import *

Alpha = 5
sigma = 5

SIGMA = BR_SIGMA(sampX, Alpha, sigma, D)        # variance
Mju = BR_Mju(sampX, sigma, SIGMA, sampy)        # mean

f_arr = Prediction(polyX, Mju)                   # prediction of mean [array]
PreSIGMA = GaussianPreSIGMA(polyX, SIGMA, n_p, D)   # prediction of variance [list]
f_l = ArrayToList(f_arr)                    # mean [list]

f_plus = []
f_sub = []
for i in range(len(f_l)):
    f_plus.append(f_l[i]+PreSIGMA[i])
    f_sub.append(f_l[i]-PreSIGMA[i])

####mean error###
error_avr = MeanSquareError(f_l, polyy_l)

'''
multi_error_list = []
for p in p_list:
    multi_error_avr = MultiErrorAverage_BR(5000, p, sampx_l_multi, sampy_l_multi, polyX, polyy_l, n_p, n_s, D)  # multi Error
    multi_error_list.append(multi_error_avr)
print multi_error_list'''
################


figure = "BR"
title = 'BR: Alpha='+str(Alpha)+',sigma='+str(sigma)+', Error='+str(error_avr)+", Sample:"+str(percent)+"%"+", K="+str(k)
PlotLines(figure, title, sampx_l, sampy_l, polyx_l, polyy_l, f_l, f_sub, f_plus)
