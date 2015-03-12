__author__ = 'gaobrook'
from P1_function import *


def Zij_EM(X, Mju, SIGMA, Pi, K, d, N):         #get the Zij
    z_ij = zeros((K, N))
    X = transpose(X)
    for j in range(K):
        for i in range(N):
            x = transpose(array([X[i]]))
            part = Pi[j]*MultiGaussian(x, Mju[j], SIGMA[j], d)
            sum = 0
            for k in range(K):
                sum += Pi[k]*MultiGaussian(x, Mju[k], SIGMA[k], d)
            z_ij[j][i] = part/sum
    return z_ij

def Nj_EM(Z_ij, K, N):                  #get Nj
    Nj = []
    for j in range(K):
        sum = 0
        for i in range(N):
            sum += Z_ij[j][i]
        Nj.append(sum)
    return array(Nj)


def NewMju_EM(Nj, Z_ij, X, K, N, d):           #calculate New Mju
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


def NewSIGMA_EM(Nj, Z_ij, Mju, X, K, N, d):   #calculate New SIGMA
    X = transpose(X)
    for j in range(K):
        SIGMA_part = zeros((d, d))
        for i in range(N):
            x = transpose(array([X[i]]))
            SIGMA_part+= Z_ij[j][i]*dot(x-Mju[j], transpose(x-Mju[j]))
        SIGMA_part = array([(1/Nj[j])*SIGMA_part])
        if(j == 0):
            SIGMA = SIGMA_part
        else:
            SIGMA = vstack((SIGMA, SIGMA_part))
    return  SIGMA



def J_EM(Z_ij, Mju, SIGMA, Pi, X, K, d, N):     #calculate J=z_ij*log(Pi*gaussian)
    X = transpose(X)
    J_value = 0
    for j in range(K):
        for i in range(N):
            x = transpose(array([X[i]]))
            gauss = MultiGaussian(x, Mju[j], SIGMA[j], d)
            J_value += Z_ij[j][i]*(gauss*Pi[j])
    return J_value



def Clustering_EM(Mju, SIGMA, Pi, X, K, d, N, maxRound, limitation):
    for p in range(maxRound):
        Z_ij = Zij_EM(X, Mju, SIGMA, Pi, K, d, N)
        Nj = Nj_EM(Z_ij, K, N)
        Pi = Nj/N
        Mju = NewMju_EM(Nj, Z_ij, X, K, N, d)
        SIGMA = NewSIGMA_EM(Nj, Z_ij, Mju, X, K, N, d)
        J = J_EM(Z_ij, Mju, SIGMA, Pi, X, K, d, N)
       # if(p != 0):
        #    sub = J - J_last
        #    if(abs(sub) < limitation):
           # if(J == J_last):
       #         print 'p='+str(p)+', J='+str(J)
       #         break
        J_last = J
        print "Round ="+str(p)
        print 'p='+str(p)+', J='+str(J)
        print "            "

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

