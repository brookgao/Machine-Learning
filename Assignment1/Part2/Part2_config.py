__author__ = 'gaobrook'
from Part2_function import *
from Assignment1.Part1.Part1_function import *
from math import *

testx_l = open('../PA-1-data-text/count_data_testx.txt').readlines()
testy_l = str(open('../PA-1-data-text/count_data_testy.txt').read()).split()
trainx_l = open('../PA-1-data-text/count_data_trainx.txt').readlines()
trainy_l = str(open('../PA-1-data-text/count_data_trainy.txt').read()).split()

D = 9

trainX = Txt_to_Mix(trainx_l, D, 400)
trainy = array([trainy_l], dtype=float).transpose()
testX = Txt_to_Mix(testx_l, D, 600)
testy = array([testy_l], dtype=float).transpose()


#### other transformation###
'''
#testX_3 = power(math.e, testX**2)
#trainX_3 = power(math.e, trainX**2)
testX_3 = log2(testX**2)
trainX_3 = log2(trainX**2)

testX = vstack((testX, testX**2))   #### question b : 2nd order polynomial
trainX = vstack((trainX, trainX**2))

testX = vstack((testX, testX_3)) #### question b : 2nd order polynomial
trainX = vstack((trainX, trainX_3))
D = 27
'''
n_tr = 400
n_te = 600





