__author__ = 'gaobrook'

from config import *
import datetime as dt
import time


choose = 1   ### 1:SVM  2:Bayes  3:KNN

dimList = [25, 50, 100, 150, 200, 300, 450, 600, 784]
trials = 2
accuracyList = {0: [], 1: [], 2: []}
accuracyTotal = {0: {0: [], 1: []}, 1: {0: [], 1: []}, 2: {0: [], 1: []}}

time_pca = {0: {0: [], 1: []}, 1: {0: [], 1: []}, 2: {0: [], 1: []}}
time_clf = {0: {0: [], 1: []}, 1: {0: [], 1: []}, 2: {0: [], 1: []}}
time_total = {0: {0: [], 1: []}, 1: {0: [], 1: []}, 2: {0: [], 1: []}}

########KNN
KNeighbors = {0: 1, 1: 2, 2: 4}

########svm
kernel_method = {0: 'poly', 1: 'linear', 2: 'rbf'}
c_rbf = {0: [2, 8, 8, 8, 8, 8, 8, 2, 8], 1: [8, 8, 2, 2, 2, 2, 2, 2, 8]}
gma_rbf = {0: [0.0078125, 0.0078125, 0.0078125, 0.0078125, 0.0078125, 0.0078125, 0.0078125, 0.0078125, 0.0078125],
           1: [0.0078125, 0.0078125, 0.0078125, 0.0078125, 0.0078125, 0.0078125, 0.0078125, 0.0078125, 0.0078125]}

########bayes
bayes_type = {0: 0, 1: 1, 2: 2}
bayes_method = {0: 'MultinomialNB', 1: 'GaussianNB', 2: "BernoulliNB"}

for k in range(3):
    if(choose == 2 and k==0): continue
    if(choose == 1):
        kernel = kernel_method[k]  ##svm
    elif(choose == 2):
        type = bayes_type[k]       ##bayes
    elif(choose == 3):
        neign = KNeighbors[k]      ##knn
    accuracyDic = {0: [], 1: []}

    for tr in range(trials):
        d = 0
        for dim in dimList:
            t_start = dt.datetime.now()

            print "=============Classification START==============="
            print "PCA start: reduce dimensions to "+str(dim)

           # digits_vec = digits_vec_total/255.0*2-1
            min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
            digits_vec = min_max_scaler.fit_transform(digits_vec_total)

            if(dim != 784):
                pca = PCA(n_components=dim)                     ####dimension reduction, PCA
                digits_vec_re = pca.fit_transform(digits_vec)
            else:
                digits_vec_re = digits_vec

            t_mid = dt.datetime.now()

            if(tr == 0):
                digits_vec_train_re = digits_vec_re[0:2000]
                #digits_vec_test_re = digits_vec_re[2000:4000]
                digits_vec_test_re = digits_vec_re[4000:4050]
            else:
                digits_vec_train_re = digits_vec_re[2000:4000]
                #digits_vec_test_re = digits_vec_re[0:2000]
                digits_vec_test_re = digits_vec_re[4000:4050]

            if(dim != 784):
                var_ratio = (pca.explained_variance_ratio_)       ###integrity  percentage
                ratio_sum = computeRatioSum(var_ratio, dim)
            print "Ratio sum = "+str(ratio_sum)

            if(choose == 1):
                if(kernel == 'rbf'):
                   print "ddddddddddd ="+str(d)
                   label_predict = ClassificationSVM(digits_vec_train_re, digits_labels_train, digits_vec_test_re, kernel, c_rbf[tr][d], gma_rbf[tr][d])
                else:
                   label_predict = ClassificationSVM(digits_vec_train_re, digits_labels_train, digits_vec_test_re, kernel)     ####  SVM
                d += 1
            elif(choose == 2):
                label_predict = ClassificationNaiveBayes(digits_vec_train_re, digits_labels_train, digits_vec_test_re, type)
            elif(choose == 3):
                label_predict = ClassificationKNN(digits_vec_train_re, digits_labels_train, digits_vec_test_re, neign)

            accuracy = computeAccuracy(label_predict, digits_labels_test)    # calculate the accuracy
            accuracyDic[tr].append(accuracy)
            print "Accuracy= "+str(accuracy)
            print "======================CLF DONE=================="
            print ""

            #####compute time costs###
            t_end = dt.datetime.now()
            t_pca = t_mid - t_start
            t_clf = t_end - t_mid
            t_total = t_end - t_start
            time_pca[k][tr].append(float(str(t_pca)[5:]))
            time_clf[k][tr].append(float(str(t_clf)[5:]))
            time_total[k][tr].append(float(str(t_total)[5:]))

    for i in range(len(dimList)):
        accuracyList[k].append((accuracyDic[0][i]+accuracyDic[1][i])/float(2.0))
    accuracyTotal[k][0].append(accuracyDic[0])
    accuracyTotal[k][1].append(accuracyDic[1])

########output#####
print accuracyList[0]
print accuracyList[1]
print accuracyList[2]

print accuracyTotal[0]
print accuracyTotal[1]
print accuracyTotal[2]
'''
for k in range(3):
    if(choose == 1):
        ord = kernel_method[k]
        print "SVM kernel= "+ord
    elif(choose == 2):
        ord = bayes_method[k]
        print "Bayes method= "+ord
    elif(choose == 3):
        ord = KNeighbors[k]
        print "KNN, K="+str(ord)

    print time_pca[k][0]
    print time_clf[k][0]
    print time_total[k][0]

    print time_pca[k][1]
    print time_clf[k][1]
    print time_total[k][1]
'''



