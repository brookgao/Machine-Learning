__author__ = 'gaobrook'
from P1_function import *


def Peak_MeanShift(X, d, N, h, maxRound, limitation):
    I = eye(d)
    SIMGA = pow(h, 2)*I
    X = transpose(X)
    for n in range(N):
        x_t = transpose(array([X[n]]))
        sum = 0
        array_sum = zeros((d, 1))
        for t in range(maxRound):
            for i in range(N):
                x_i = transpose(array([X[i]]))
                gauss = MultiGaussian(x_i, x_t, SIMGA, d)
                sum += gauss
                array_sum += x_i*gauss
            x_t = array_sum/sum
            if(t != 0):
                sub = abs(x_t - x_last) < limitation
                T = array([[True], [True]])
                res = any(sub == T)
                if(res):
                    print 'Iterate t='+str(t)
                    break
            x_last = x_t
            print 'N = '+str(n)+', Round ='+str(t)+" :"
            print x_t
            print "           "
        if(n == 0):
            X_peak = x_t
        else:
            X_peak = hstack((X_peak, x_t))

    return X_peak

def Clustering_MeanShift(X, X_peak, N, d, cluster_gap):
    X = transpose(X)
    X_peak = transpose(X_peak)
    Y = []
    for i in range(N):
        x_peak = array([X_peak[i]])
        x = array([X[i]])
        HasClass = False
        if(i == 0):
            peak_cluster = {0: x_peak}
            cluster = {0: x}
            Y.append(1)
        else:
            for k in range(len(cluster)):
                J = peak_cluster[k].shape[0]
                peak_cluster_k = ones((1, d))

                for i in range(d):
                    average = 0
                    for j in range(J):
                        average += peak_cluster[k][j][i]
                    peak_cluster_k[0][i] = average/J

                sub = abs(x_peak - peak_cluster_k) < cluster_gap
                T = ones((d, 1)) > 0
                res = any(sub == T)
                if(res):
                    peak_cluster[k] = vstack((peak_cluster[k], x_peak))
                    cluster[k] = vstack((cluster[k], x))
                    Y.append(k+1)
                    HasClass = True
                    break
            if(HasClass == False):
                peak_cluster[len(peak_cluster)] = x_peak
                cluster[len(peak_cluster)-1] = x
                Y.append(len(peak_cluster))
    print 'peak=', peak_cluster
    print 'cluster=', cluster
    print Y
    return cluster, array([Y])

def PlotCluster_MeanShift(figure, title, cluster):
    plt.figure(figure)
    plt.title(title)
    color = ['go', 'bo', 'ro', 'co', 'ko', 'yo', 'mo', 'wo', 'k^', 'y^', 'm^', 'w^', 'g^', 'b^', 'r^', 'c^']
    for k in range(len(cluster)):
        if(k > 15):
            break
        else:
            c = transpose(cluster[k])
            plt.plot(c[0], c[1], color[k], label='k:'+str(k+1))
    plt.axis([-20, 20, -20, 20])
    plt.legend(loc=3)
    plt.grid(True)
    plt.show()