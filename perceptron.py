import Classifier
import sys

''' 
	Execution: 
	python id3.py </trainData.csv> </testData.csv> <eta> </MFN> 
	1 trainData - csv file contating training data
	2 testData - csv file contatining test data
	3 eta - learning rate
	4 MFN - model file name (all one word ex: XORmodel)
'''

def main():
	print "training data file: " + str(sys.argv[1]) 
	file = open(str(sys.argv[1]))
	"""
	IMPORTANT: Change this variable too change target attribute 
	"""
	target = "Class"
	#extract training data
	data = [[]]
	for line in file:
		line = line.strip("\r\n")
		data.append(line.split(','))
	file.close()
	data.remove([])
	attributes = data[0]
	data.remove(attributes)
	expected = []
	i = 0
	for entry in data:
		expect = int(entry[len(entry)-1])
		if i == 0:
			length = len(entry) - 1
		expected.append(expect)
		entry.pop()
		i = i+1
	
	#data = [[1,0,1,1,0],[0,0,1,1,1],[1,1,1,0,0]]
	eta = float(sys.argv[3])
	#Perceptron
	f = open(str(sys.argv[4])+ ".model", 'w')
	#write to model, and collect weights
	weights = Classifier.createPerceptron(data, eta, expected, length, attributes, f)
	f.close()
	
	data = [[]]
	print "test data file: " + str(sys.argv[2])
	file = open(str(sys.argv[2]))
	for line in file:
		line = line.strip("\r\n")
		data.append(line.split(','))
	data.remove([])
	data.remove(attributes)
	expected = []
	print len(data)
	i = 0
	correct = 0
	for entry in data:
		expect = int(entry[len(entry)-1])
		if i == 0:
			length = len(entry) - 1
		expected.append(expect)
		entry.pop()
		j = 0
		result = 0
		for point in entry:
			if point == '0':
				if float(weights[j]) < 0:
					result += float(weights[j])	
			else:
				if float(weights[j]) > 0:
					result += float(weights[j])
			j = j + 1
		if result > 0:
			spam = True
			if expected[i] == 1:
				correct = correct + 1
		else:
			spam = False
			if expected[i] == 0:
				correct = correct + 1
		print str(i+1) + ": " + str(result) + " => " + str(spam) 
		i = i+1
	accuracy = float(correct)/i * 100
	print str(accuracy) + "% correctly identified"
		
if __name__ == '__main__':
	main()