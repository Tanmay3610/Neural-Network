# Neural Network of just three Layers 
# First Layer: Input Layer
# Second Layer : Hidden Layer
# Third Layer : Output Layer

# Activation Fucntion Used : Sigmoid Function
import numpy as np
np.random.seed(np.random.randint(0, 100))

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def dsigmoid(x):
    return np.matmul(x, np.transpose(np.subtract(1, x)))

class NeuralNetwork:
    def __init__(self, numI, numH, numO):
        self.number_of_input = numI
        self.number_of_hidden = numH
        self.number_of_output = numO
        self.learning_rate = 0.1

        self.weights_ih = 0.1 * np.random.randn(self.number_of_input, self.number_of_hidden)
        self.weights_ho = 0.1 * np.random.randn(self.number_of_hidden, self.number_of_output)

        self.bias_hidden = np.zeros((1, numH))
        self.bias_output = np.zeros((1, numO))

    def feedForward(self, input):
        # from input to hidden layer
        self.output_from_hidden = sigmoid(np.matmul(input, self.weights_ih) + self.bias_hidden)
        
        #from hidden to output
        final_output = sigmoid(np.matmul(self.output_from_hidden, self.weights_ho) + self.bias_output)
        
        return final_output

    def train(self, inputs, target):
        #Error
        guess = self.feedForward(inputs)
        error = target - guess
        
        #calculating delta W for hidden to output
        delta_weights_ho = self.learning_rate * np.matmul(np.matmul(error, dsigmoid(guess)), self.output_from_hidden)
        delta_weights_ho = np.transpose(delta_weights_ho)
        self.weights_ho = self.weights_ho + delta_weights_ho
        
        #calculationg the bias change for hidden to output
        self.bias_output = self.bias_output + np.transpose(np.matmul(error, dsigmoid(guess)) * self.learning_rate)
        
        #calculating delta W for input to hidden
        hidden_error = np.matmul(self.weights_ho, error)
        delta_weights_ih = self.learning_rate * np.matmul(np.matmul(hidden_error, dsigmoid(self.output_from_hidden)), np.mat(inputs))
        self.weights_ih = self.weights_ih + delta_weights_ih

        #calculationg the bias change for input to hidden
        self.bias_hidden = self.bias_hidden + np.transpose(np.matmul(hidden_error, dsigmoid(self.output_from_hidden)) * self.learning_rate)

# Params to be passed into contructor:
# 1 param - number of neurons in Input layer
# 2 param - number of neurons in hidden layer
# 3 param - number of neurons in output layer

brain = NeuralNetwork(4, 4, 1)
for i in range(7000):
    count = np.random.randint(0, len(X_train))
    brain.train(X_train[count], y_train[count])

