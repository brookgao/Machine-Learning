__author__ = 'gaobrook'
from function import *

digits_vec = open('digits4000_txt/digits4000_digits_vec.txt').readlines()
digits_labels = open('digits4000_txt/digits4000_digits_labels.txt').read().split()
cdigits_vec = open('challenge/cdigits_cdigits_vec.txt').readlines()
cdigits_labels = open('challenge/cdigits_cdigits_labels.txt').readlines()


digits_vec_total = txtConvertToArray(digits_vec, 4000, 784)
cdigits_vec_total = txtConvertToArray(cdigits_vec, 50, 784)
digits_vec_total = vstack((digits_vec_total, cdigits_vec_total))

digits_labels = array(digits_labels, dtype=int)
digits_labels_train = digits_labels[0:2000]
#digits_labels_test = digits_labels[2000:4000]
digits_labels_test = array(cdigits_labels, dtype=int)

