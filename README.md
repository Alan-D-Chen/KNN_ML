# KNN_ML
========================================================<br>
Demo for KNN(K-Nearest Neighbor) &amp; Iris module(a classical test) in data analysis in Python 

>>>This is a simple demo for KNN(K-Nearest Neighbor)<br>
<br>
>>Python3 Pycharm <br>


>`02.KNN(K-Nearest Neighbor)`
<br>

If you get that :<br>
`
'AttributeError: 'dict' object has no attribute 'iteritems'
`
<br>
 
 you will find some help from here:<br>
 *[help1](https://blog.csdn.net/qq_30638831/article/details/79928463)<br>
 
 <br>
 
If you get that :<br>
`
IndexError: list index out of range
`<br>
```
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)-1):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet)))*100.0
```
 
 you will find some help from here:<br>
 **[help2](https://www.cnblogs.com/hfdkd/p/7719134.html)<br>
 
 
 
 
 
 best wish for you.
