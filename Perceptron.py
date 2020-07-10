#My First Perceptron
#By: Tanmay Agarwal 
'''
    Features:
    - This perceptron has an accuracy score of 1.
    - This took dataset of 1500 points to train it.
    - I took 500 points to test it.
    - This kind of perceptrons can only be used for classification
'''
import numpy as np
np.random.seed(0)

#Making some random points in the 2-D Space
class Points:
    def __init__(self, number_of_points = 100):
        self.x = []
        self.y = []
        for i in range(number_of_points):
            self.x.append(np.random.randint(0, high = 100))
        for i in range(number_of_points):
            self.y.append(np.random.randint(0, high = 100))
        self.label = []
        for i in range(number_of_points):
            if self.x[i] > self.y[i]:
                self.label.append(1)
            else:
                self.label.append(-1)
        
    def getPoints(self):
        return (self.x, self.y, self.label)

#Making of perceptron
class Perceptron:

    def __init__(self):
        self.weights = 0.1 * np.random.randn(1, 2)
        self.weights = self.weights.flatten()
        self.learningRate = 1

    def guess(self, inputs):
        self.output = np.dot(np.transpose(self.weights), inputs)

    def activationFunction(self):
        if self.output >= 0:
            self.output = 1
        else:
            self.output = -1

    def train(self, inputs, target):
        self.guess(inputs)
        self.activationFunction()
        error = target - self.output

        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + error * inputs[i] * self.learningRate
    
    def accuracy_score(self, guess, label):
        count = 0
        for i in range(len(guess)):
            if label[i] == guess[i]:
                count = count + 1
        return count/len(guess)

    def test(self, X, y, label):
        output = []
        for i in range(len(X)):
            perceptron.guess([X[i], y[i]])
            perceptron.activationFunction()
            output.append(perceptron.output)
        return self.accuracy_score(output, label)


p = Points(2000)
X, y, label = p.getPoints()

perceptron = Perceptron()

#Checking the accuracy before training
print('Before Training:', perceptron.test(X[1500 : 2000], y[1500 : 2000], label[1500 : 2000]))

for i in range(1500):
    perceptron.train([X[i], y[i]], label[i])

#Checking the accuracy After training
print('After Training:', perceptron.test(X[1500 : 2000], y[1500 : 2000], label[1500 : 2000]))
