__author__ = 'gaobrook'
from P1_function import *

def Zij_Kmeans(X, K, N, Mju):
    z_ij = zeros((K, N))
    X = transpose(X)

    for i in range(N):
        max = 0
        k_choose = 0
        for j in range(K):
            x = transpose(array([X[i]]))
            sub = dot(transpose(x- Mju[j]), x-Mju[j])
            tmp = float(sub)
            if(tmp > max):
                max = tmp
                k_choose = j
        for j in range(K):
            if(j == k_choose):
                z_ij[j][i] = 1
            else:
                z_ij[j][i] = 0
    return z_ij

def Nj_Kmeans(Z_ij, K, N):                  #get Nj
    Nj = []
    for j in range(K):
        sum = 0
        for i in range(N):
            sum += Z_ij[j][i]
        Nj.append(sum)
    return array(Nj)


def NewMju_Kmeans(Nj, Z_ij, X, K, N, d):           #calculate New Mju
    X = transpose(X)
    for j in range(K):
        mju = zeros((1, d, 1))
        for i in range(N):
            x = transpose(array([X[i]]))
            mju += Z_ij[j][i]*array([x])
        mju = (1/Nj[j])*mju
        if(j == 0):
            Mju = mju
        else:
            Mju = vstack((Mju, mju))
    return  Mju


def Clustering_Kmeans(Mju, X, K, N, d, maxRound, limitation):

    for p in range(maxRound):
        Z_ij = Zij_Kmeans(X, K, N, Mju)
        Nj = Nj_Kmeans(Z_ij, K, N)
        #Pi = Nj/N
        Mju = NewMju_Kmeans(Nj, Z_ij, X, K, N, d)

        if(p != 0):
            sub = abs(Mju - Mju_last) < limitation
            T = array([[True], [True]])
            res = all(sub == T)
            if(res):
                break
        Mju_last = Mju
        print "maxRound ="+str(p)+":"
        print Mju

    Y = []
    for i in range(N):
        max = 0
        k_choose = 0
        for j in range(K):
            if(Z_ij[j][i] > max):
                max = Z_ij[j][i]
                k_choose = int(j+1)
        Y.append(k_choose)
    return array([Y])
