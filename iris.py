# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 下午 10:32
# @Author  : Alan D. Chen
# @FileName: descicon_tree.py
# @Software: PyCharm

from sklearn import neighbors
from sklearn import datasets

knn = neighbors.KNeighborsClassifier()

iris = datasets.load_iris()
# save data
# f = open("iris.data.csv", 'wb')
# f.write(str(iris))
# f.close()

print("Iris:\n", iris)

knn.fit(iris.data, iris.target)

predictedLabel = knn.predict([[0.1, 0.2, 0.3, 0.4]])
print("Let's get the test and predict the result:\n")
#print ("predictedLabel is :" + predictedLabel)
print("predictedLabel:\n", predictedLabel)
