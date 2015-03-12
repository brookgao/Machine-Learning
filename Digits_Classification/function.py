__author__ = 'gaobrook'
import matplotlib.pyplot as plt
from math import *
from numpy import *
from numpy.linalg import *
from random import *
from sklearn.decomposition import PCA
from sklearn.svm import *
from sklearn.datasets import *
from sklearn.linear_model import *
from sklearn.neighbors import *
from sklearn.cross_validation import *
from sklearn.naive_bayes import *
from sklearn.preprocessing import *

def txtConvertToArray(lines, row, column):     #convert txt to array
    i = 0
    Mix = zeros((row, column), dtype=float)
    for lines in lines:
        Mix[i] = array([lines.split()], dtype=float)
        i += 1
    return Mix

def computeRatioSum(var_ratio, dim):       # calculate the info percentage remaining
    ratio_sum = 0
    for i in range(dim):
        ratio_sum += var_ratio[i]
    return ratio_sum


def getOneDigitLabel(label, digit_labels, label_one, label_rest):    # get an array of classification: one label and others
    labels_new = []
    for e in digit_labels:
        if(e == label):
            labels_new.append(label_one)
        else:
            labels_new.append(label_rest)
    return array(labels_new)


def ClassificationSVM(digits_vec_train, digits_labels, digits_vec_test, kernel_method='rbf', c=1.0, gma=0.0):
    clf = []
    print "Ready to generate SVM clf, kernel="+kernel_method
    print "====clf fit START===="
    for i in range(10):
        label_train = getOneDigitLabel(i, digits_labels, 1, -1)   #list for one label
        c_sub = SVC(kernel=kernel_method, C=c, gamma=gma)
        c_sub.fit(digits_vec_train, label_train)
        clf.append(c_sub)
        print "No."+str(i)+" SVM cfl completed"

    print "====clf predict START==="
    predict = []
    n = digits_vec_test.shape[0]
    predict_total = {}
    confidence_total = {}

    for j in range(10):
        predict_total[j] = clf[j].predict(digits_vec_test)
        confidence_total[j] = clf[j].decision_function(digits_vec_test)

    for i in range(n):
        best_pre = -1
        max_confidence = -999

        for j in range(10):
            if(confidence_total[j][i] > max_confidence):
                best_pre = j
                max_confidence = confidence_total[j][i]
       # print "i="+str(i)+", pre="+str(best_pre)+", confidence="+str(max_confidence)
        predict.append(best_pre)

    #print "The predicting result: "+str(predict)
    return array(predict)


def ClassificationKNN(digits_vec_train, digits_labels, digits_vec_test, K=1):
    print "Ready to generate KNN clf, K="+str(K)+":"
    neigh = KNeighborsClassifier(n_neighbors=K)
    neigh.fit(digits_vec_train, digits_labels)
    predit = neigh.predict(digits_vec_test)
    return predit


def ClassificationNaiveBayes(digits_vec_train, digits_labels, digits_vec_test, type):
    bayes_method = {0: "MultinomialNB", 1: "GaussianNB", 2: "BernoulliNB"}
    print "Ready to generate Naive_Bayes clf, type="+bayes_method[type]
    if(type == 0):
        clf = MultinomialNB()
    elif(type == 1):
        clf = GaussianNB()
    elif(type == 2):
        clf = BernoulliNB()
    clf.fit(digits_vec_train, digits_labels)
    predict = clf.predict(digits_vec_test)
    return predict

def computeAccuracy(label_predict, label_original):
    n = label_predict.shape[0]
    sum = 0
    for i in range(n):
        if(label_predict[i] == label_original[i]):
            sum += 1
    accuracy = sum/float(n)
    return accuracy


def plotPredictDigits(digits_vec, label_predict, label_original):
    n = label_predict.shape[0]
    plt.figure(figsize=(12, 10))
    NIMAGES=15
    order = 1
    for i in range(n):
        if(label_predict[i]!=label_original[i]):
            plt.subplot(8, 15, order)
            plt.axis('off')
            plt.imshow(digits_vec[i].reshape(28, 28).transpose(), cmap=plt.cm.gray)
            plt.title("pre:"+str(label_predict[i]))
            order += 1
    plt.show()


def getCrossValidationData(digits_vec_train, trial):
    row = digits_vec_train.shape[0]
    dim = digits_vec_train.shape[1]
    filename = "/Users/gaobrook/Desktop/libsvm-3.20/tools/rbf_dim"+str(dim)+"_trial"+str(trial)
    f = open(filename, "w")
    for i in range(row):
        label = divmod(i, 200)[0]
        f.write(str(label)+" ")
        for j in range(dim):
            f.write(str(j)+":"+str(digits_vec_train[i][j])+" ")
        f.write('\n')
    f.close()




