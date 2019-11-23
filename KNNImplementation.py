# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 下午 10:32
# @Author  : Alan D. Chen
# @FileName: KNN.py
# @Software: PyCharm

import csv
import random
import math
import operator


def loadDataset(filename, split, trainingSet = [], testSet = []):
    with open(filename, 'rt') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):####行数######
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):########维度为length######
        distance += pow((instance1[x]-instance2[x]), 2)
    return math.sqrt(distance)


def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        #testinstance
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
        #distances.append(dist)
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
        return neighbors


def getResponse(neighbors):
    classVotes = {}
    #print(classVotes)
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
            #print(classVotes[response])
        else:
            classVotes[response] = 1
            #print(classVotes[response])
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


def getAccuracy(testSet, predictions):
    correct = 0
    print("#%#the length of testSet:\n", len(testSet))
    for x in range(len(testSet)-1):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet)))*100.0


def main():
    #prepare data
    trainingSet = []
    testSet = []
    print("Please input a number for dividing the dataset into 2 parts, trainingset and testset.\n To make sure that trainingset is bigger then testset,the number is bigger then 0.5,: ")
    split_ = input()
    split = float(split_)

    print("trainingSet:\n",trainingSet,"\n testSet: \n", testSet)
    print("the length of trainingSet:\n", len(trainingSet))
    print("the length of testSet:\n", len(testSet))
    loadDataset(r'E:/dataset/dataset_1/02KNN/irisdata.txt', split, trainingSet, testSet)
    print('Training set: \n' + repr(len(trainingSet)))
    print('Testing set: \n' + repr(len(testSet)))
    #generate predictions
    predictions = []
    print("the length of predictions:\n", len(predictions))
    k = 3
    for x in range(len(testSet)):
        # trainingsettrainingSet[x]


        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        # #print("#############################################")
        # print('predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
        # #print("#############################################")

    print("the length of testSet:\n", len(testSet))
    print(predictions)
    print("the length of predictions:\n", len(predictions))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: \n' + repr(accuracy) + '%')

if __name__ == '__main__':
    main()































