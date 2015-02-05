from random import choice
from numpy import array, dot, random
import numpy as np

# The unit step function, equal to 0 for x < 0 and 1 for x >= 0.
unitStep = lambda x: 0 if x < 0 else 1

# createPerceptron() returns a list of weights
# arg: data 		- 	training data 
# arg: eta 			- 	learning rate
# arg: expected 	- 	list of solutions for training data
# arg: length		- 	size of the training data
# arg: attributes 	- 	features of data
# arg: f 			- 	write to file
# IN ORDER TO FIND IDEAL WEIGHTS I REDUCE THE ERROR MAGNITUDE TO ZERO.
def createPerceptron(data, eta, expected, length, attributes, f):
	#turn string elements into float elements
	trainData = np.array(data, dtype=float)
	#need length (size of the training data) number of random numbers
	w = random.rand(length)
	#run 100 interations - instructions
	n = 100
	
	for i in xrange(n):
		# Pick random sample from training data floats lists
		x = choice(trainData)
		# Calculate dot product with current weights and random sample
		result = dot(w, x)
		# Compare with answer
		error = expected[i] - unitStep(result)
		# Make changes to the weights based off random sampling
		w += eta * error * x
	
	# WRITE TO MODEL FILE
	etaString = str(eta) + '\n'
	f.write(etaString)
	i = 0
	for attribute in attributes:
		if i < len(attributes) - 1: 
			fileLine = str(attribute) + " " + str(w[i]) + '\n'
			f.write(fileLine)
			i = i + 1
			
	return w
			
			