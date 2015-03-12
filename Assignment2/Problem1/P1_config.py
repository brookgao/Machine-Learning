__author__ = 'gaobrook'
from P1_function import *

dataA_X = open('cluster_data_text/cluster_data_dataA_X.txt').readlines()
dataA_Y = open('cluster_data_text/cluster_data_dataA_Y.txt').read().split()
dataB_X = open('cluster_data_text/cluster_data_dataB_X.txt').readlines()
dataB_Y = open('cluster_data_text/cluster_data_dataB_Y.txt').read().split()
dataC_X = open('cluster_data_text/cluster_data_dataC_X.txt').readlines()
dataC_Y = open('cluster_data_text/cluster_data_dataC_Y.txt').read().split()

dataA_X = TextConvertToMix(dataA_X, 2, 200)
dataA_Y = ListToArray(dataA_Y)

dataB_X = TextConvertToMix(dataB_X, 2, 200)
dataB_Y = ListToArray(dataB_Y)

dataC_X = TextConvertToMix(dataC_X, 2, 200)
dataC_Y = ListToArray(dataC_Y)





