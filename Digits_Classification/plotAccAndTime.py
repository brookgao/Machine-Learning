__author__ = 'gaobrook'
from config import *
from io import StringIO
import pandas as pd

##dim = 25
accuracy = [93.875, 86.05, 95.275, 92.675, 91.325, 92.9, 81.175, 85.775, 68.95]
time = [1.8441165, 2.8413465, 1.850789, 2.0935915, 2.07596, 2.5734465, 1.0752575, 1.223989, 1.034903]

##dim=25
s = StringIO(u'''\
                accuracy     time
SVM_POLY         93.875   1.8441165
SVM_LINEAR       86.05    2.8413465
SVM_RBF          95.275   1.850789
KNN-1            92.675   2.0935915
KNN-2            91.325   2.07596
KNN-4            92.9     2.5734465
MultinomialNB    81.175   1.0752575
GaussianNB       85.775   1.223989
BernoulliNB      68.95    1.034903''')



df = pd.read_csv(s, index_col=0, delimiter=' ', skipinitialspace=True)

fig = plt.figure()       # Create matplotlib figure
title = "Accuracy and Time efficacy Comparison(dimension = 25)"


ax = fig.add_subplot(111) # Create matplotlib axes
ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.

width_a = 0.45
width_t = 0.25
df.accuracy.plot(kind='bar', color='red', ax=ax, width=width_a, position=0.5, label="accuracy")
df.time.plot(kind='bar', color='cyan', ax=ax2, width=width_t, position=0.55, label="time")

ax.set_ylabel('Accuracy(%)')
ax.set_ylim(60, 100)
ax2.set_ylabel('Time(s)')
ax2.set_ylim(0, 6)
ax.legend(loc=2)
ax2.legend(loc=1)

plt.xlabel("classifiers")
plt.title(title)
plt.show()
