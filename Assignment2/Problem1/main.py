__author__ = 'gaobrook'
from P1_config import *
from EM import *
from K_means import *
from Mean_shift import *

d = 2
K = 4
N = dataA_X.shape[1]
maxRound = 5
limitation = 0.1
data_X = dataA_X

#####True Clustering####

'''
figure = 'True'
title = 'True clustering, dataC_X'
print dataC_Y.shape
PlotCluster(figure, title, dataC_X, dataC_Y, N)
'''


#####EM-GMM#######
'''
SIGMA = RandomSIGMA(0.1, 1, K, d)
Mju = RandomMju(0, 1, K, d)
Pi = [0.2, 0.3, 0.1, 0.2]

data_Y_EM = Clustering_EM(Mju, SIGMA, Pi, data_X, K, d, N, maxRound, limitation)

figure = "EM"
title = "EM-GMM, dataA"
PlotCluster(figure, title, data_X, data_Y_EM, N)
'''
#########EM-GMM##########



#####K-means#######
'''
Mju = RandomMju(0, 1, K, 2)
data_Y_Kmeans = Clustering_Kmeans(Mju, data_X, K, N, d, maxRound, limitation)
figure = "K-means"
title = "K-means, dataB"
PlotCluster(figure, title, data_X, data_Y_Kmeans, N)
########K-means######
'''



#####Mean_shift####

h = 2
cluster_gap = 0.5
figure = 'Mean-shift'
title = 'Mean-shift, dataA, Bandwidth h='+str(h)
X_peak = Peak_MeanShift(data_X, d, N, h, maxRound, limitation)
f = open('/Users/gaobrook/Desktop/Clustering/peak.txt', 'w+')
f.writelines(unicode(X_peak))
f.close()

cluster = Clustering_MeanShift(data_X, X_peak, N, d, cluster_gap)
print cluster[1]

PlotCluster_MeanShift(figure, title, cluster[0])

#####Mean_shift#####



