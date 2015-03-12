__author__ = 'gaobrook'
from Part1_function import *

sampx_l = str(open('../PA-1-data-text/polydata_data_sampx.txt').read()).split()
sampy_l = str(open('../PA-1-data-text/polydata_data_sampy.txt').read()).split()
polyx_l = str(open('../PA-1-data-text/polydata_data_polyx.txt').read()).split()
polyy_l = str(open('../PA-1-data-text/polydata_data_polyy.txt').read()).split()

k = 10
D = k+1
n_s = len(sampx_l)                  # number of sample x,y
n_p = len(polyx_l)                  # number of poly x,y
percent = 100
num = int(0.01*percent*n_s)
sampx_l_multi = sampx_l
sampy_l_multi = sampy_l


polyx_l = ListStrToFloat(polyx_l)
polyy_l = ListStrToFloat(polyy_l)

polyx = ListToArray(polyx_l)
polyy = ListToArray(polyy_l).transpose()

polyX = GenerateX(polyx, D, n_p)    # X_Input


New = RandomList(sampx_l, sampy_l, percent, n_s, D)
sampx_l = New[0]
sampy_l = New[1]
sampx = New[2]
sampy = New[3]
###adding some outliers to sampy###
'''
sampy[0] = sampy[0]+100
sampy[15] = sampy[5]+150
sampy[30] = sampy[30]+100
sampy[45] = sampy[45]+200
print sampy
'''
sampX = New[4]


p_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]