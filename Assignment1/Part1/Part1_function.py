from scipy import *
import matplotlib.pyplot as plt
from numpy import *
from numpy.linalg import *
from random import *
import scipy.optimize as opt

##########common function################
def ListStrToFloat(list):       # str to float in a list
    list_float = []
    for i in range(len(list)):
        list_float.append(float(list[i]))
    return list_float

def ListToArray(list):               # convert list to array
    arr = array([list], dtype=float)
    return arr

def ArrayToList(array):
    list = []
    for i in range(len(array)):
        list.append(float(array[i]))
    return list

def GenerateX(x_array, D, n):         # combine x1,x2,x3...xn
    X_mix = zeros((D, n))
    for i in range(D):
        for j in range(n):
            X_mix[i][j] = (x_array[0][j])**i
    return X_mix

def Prediction(x, Thet):             # get the prediction of f according to inputx
    f = dot(x.transpose(), Thet)
    return f

def PlotLines(figure, title, sampx_l, sampy_l, polyx_l, polyy_l,f_l, PreMju_sub=None, PreMju_plus=None):
    plt.figure(figure)
    plt.title(title)
    plt.plot(sampx_l, sampy_l, "o", label="sample")
    plt.plot(polyx_l, f_l, "g-", label="prediction")
    if(figure == 'BR'):
        plt.plot(polyx_l, PreMju_sub, "c-", label="Prediction Mju-(sigma**1/2)")
        plt.plot(polyx_l, PreMju_plus, "c-", label="Prediction Mju+(sigma**1/2)")
    plt.plot(polyx_l, polyy_l, "r-", label="poly")
    plt.legend(loc=3)
  #  plt.savefig('/Users/gaobrook/Desktop/Regression/d/'+figure+'.jpg', dpi=200)
    plt.show()

def MeanSquareError(f_l, polyy):        # mean-square error
    sum = 0
    n = len(polyy)
    for i in range(n):
        error = f_l[i]-polyy[i]
        sum += (error**2)
    avr = sum/n
    return avr

def RandomList(sampx_l, sampy_l, percent, total, D):  # random samples:10% 30%...100%
    number = int(percent*0.01*total)
    if(percent != 100):
        rlist = [randint(0, total-1) for i in range(number)]
        sampx_l_new = []
        sampy_l_new = []
        for e in rlist:
            sampx_l_new.append(sampx_l[e])
            sampy_l_new.append(sampy_l[e])
    else:
        sampx_l_new = sampx_l
        sampy_l_new = sampy_l
    sampx_new = ListToArray(sampx_l_new)
    sampy_new = ListToArray(sampy_l_new).transpose()
    sampX_new = GenerateX(sampx_new, D, number)
    return sampx_l_new, sampy_l_new,sampx_new,sampy_new,sampX_new


#########LS function####
def LS(sampX, sampy):             # get the parameter
    temp1 = inv(dot(sampX, sampX.transpose()))
    temp2 = dot(sampX, sampy)
    Thet = dot(temp1, temp2)
    return Thet

def MultiErrorAverage_LS(times, per, sampx_l_multi, sampy_l_multi, polyX, polyy_l, n_s, D):
    error_sum = 0
    for i in range(times):
        New = RandomList(sampx_l_multi, sampy_l_multi, per, n_s, D)
        sampx_l = New[0]
        sampy_l = New[1]
        sampx = New[2]
        sampy = New[3]
        sampX = New[4]
        Thet = LS(sampX, sampy)                     # parameters
        f_pre = Prediction(polyX, Thet)             # prediction of y
        f_l = ArrayToList(f_pre)                    # convert array[Y] into list
        error_avr = MeanSquareError(f_l, polyy_l)   # average error
        error_sum += error_avr
    return (error_sum/times)


##### RLS function #####
def RLS(sampX, sampy, Lambda, D):
    temp1 = dot(sampX, sampX.transpose())
    temp2 = Lambda*eye(D)
    temp3 = dot(sampX, sampy)
    Thet = dot(inv(temp1+temp2), temp3)
    return Thet

def MultiErrorAverage_RLS(times, per, sampx_l_multi, sampy_l_multi, polyX, polyy_l, n_s, D):
    error_sum = 0
    for i in range(times):
        New = RandomList(sampx_l_multi, sampy_l_multi, per, n_s, D)
        sampx_l = New[0]
        sampy_l = New[1]
        sampx = New[2]
        sampy = New[3]
        sampX = New[4]

        Lambda = 0.4
        Thet = RLS(sampX, sampy, Lambda, D)
        f_pre = Prediction(polyX, Thet)
        f_l = ArrayToList(f_pre)

        error_avr = MeanSquareError(f_l, polyy_l)   # average error
        error_sum += error_avr
    return (error_sum/times)

#### LASSO function#####
def lassoH(sampX):   # format H
    temp1 = vstack((dot(sampX, sampX.transpose()), dot(-sampX, sampX.transpose())))
    temp2 = vstack((dot(-sampX, sampX.transpose()), dot(sampX, sampX.transpose())))
    H = hstack((temp1, temp2))
    return H

def quadprogX(D, H, sampX, sampy, Lambda): # 0.5*dot(dot(x.transpose(), H), x)+dot(f.transpose(), x)
    f1 = dot(sampX, sampy)
    f2 = dot(-sampX, sampy)
    f = Lambda*ones((2*D, 1))-vstack((f1, f2))
    X = zeros((2*D, 1))

    fun = lambda x: float(0.5*dot(dot(x.transpose(), H), x)+dot(f.transpose(), x))
    cons = ({'type': 'ineq', 'fun': lambda x: x})
    res = opt.minimize(fun, X, constraints=cons, method="SLSQP")
    return res

def MultiErrorAverage_LASSO(times, per, sampx_l_multi, sampy_l_multi, polyX, polyy_l, n_s, D):
    error_sum = 0
    for i in range(times):
        New = RandomList(sampx_l_multi, sampy_l_multi, per, n_s, D)
        sampx_l = New[0]
        sampy_l = New[1]
        sampx = New[2]
        sampy = New[3]
        sampX = New[4]

        Lambda = 0.5

        H = lassoH(sampX)  #get the H
        Thet_mix = quadprogX(D, H, sampX, sampy, Lambda).x
        Thet_plus = ListToArray(Thet_mix[0:D])
        Thet_sub = ListToArray(Thet_mix[D:2*D])
        Thet = (Thet_plus-Thet_sub).transpose()

        f_pre = Prediction(polyX, Thet)
        f_l = ArrayToList(f_pre)

        error_avr = MeanSquareError(f_l, polyy_l)   # average error
        error_sum += error_avr
    return (error_sum/times)



##### BR function ######
def BR_SIGMA(sampX, Alpha, sigma, D):             # get the variance sigma2
    temp = (1/float(sigma))*dot(sampX, sampX.transpose())
    SIGMA = inv(temp+(1/float(Alpha))*eye(D))
    return SIGMA

def BR_Mju(sampX, sigma, SIGMA, sampy):      # get the mean Mju
    temp = dot(sampX, sampy)
    Mju = dot((1/float(sigma))*SIGMA, temp)
    return Mju

def GaussianPreSIGMA(polyX, SIGMA, n_p, D):
    PreSIGMA = []
    for i in range(n_p):
       temp1 = polyX[0:D, i]
       temp2 = dot(dot(temp1.transpose(), SIGMA), temp1)
       PreSIGMA.append(temp2**0.5)
    return PreSIGMA

def MultiErrorAverage_BR(times, per, sampx_l_multi, sampy_l_multi, polyX, polyy_l, n_p, n_s, D):
    error_sum = 0
    for i in range(times):
        New = RandomList(sampx_l_multi, sampy_l_multi, per, n_s, D)
        sampx_l = New[0]
        sampy_l = New[1]
        sampx = New[2]
        sampy = New[3]
        sampX = New[4]

        Alpha = 5
        sigma = 5
        SIGMA = BR_SIGMA(sampX, Alpha, sigma, D)        # variance
        Mju = BR_Mju(sampX, sigma, SIGMA, sampy)        # mean

        PreMju_arr = Prediction(polyX, Mju)                   # prediction of mean [array]
        PreSIGMA = GaussianPreSIGMA(polyX, SIGMA, n_p, D)   # prediction of variance [list]
        PreMju = ArrayToList(PreMju_arr)                    # mean [list]

        error_avr = MeanSquareError(PreMju, polyy_l)    # average error
        error_sum += error_avr
    return (error_sum/times)

###### RR function########
def robustA(sampX, n):                      # format A
    I = eye(n)
    temp1 = vstack((-sampX.transpose(), sampX.transpose()))
    temp2 = vstack((-I, -I))
    A = hstack((temp1, temp2))
    return A

def linprogX(D, n_s, A, sampy):           # minimize dot(f.transpose, X)
    f1 = zeros((D, 1))
    f2 = ones((n_s, 1))
    f = vstack((f1, f2))
    b = vstack((-sampy, sampy))
    X = zeros((D+n_s, 1))
    B = ArrayToList(b)                   # B must be a scalar

    fun = lambda x: dot(f.transpose(), x)
    cons = ({'type': 'ineq', 'fun': lambda x: B-dot(A, x)})
    res = opt.minimize(fun, X, constraints=cons, method="SLSQP")
    return res

def MultiErrorAverage_RR(times, per, sampx_l_multi, sampy_l_multi, polyX, polyy_l, n_s, D):
    error_sum = 0
    num = int(0.01*per*n_s)
    for i in range(times):
        New = RandomList(sampx_l_multi, sampy_l_multi, per, n_s, D)
        sampx_l = New[0]
        sampy_l = New[1]
        sampx = New[2]
        sampy = New[3]
        sampX = New[4]

        A = robustA(sampX, num)                 # get the A
        X = linprogX(D, num, A, sampy).x
        Thet = ListToArray(X[0:D]).transpose()

        f_pre = Prediction(polyX, Thet)
        f_l = ArrayToList(f_pre)
        error_avr = MeanSquareError(f_l, polyy_l)
        error_sum += error_avr
    return (error_sum/times)