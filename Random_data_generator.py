import sys
import numpy as np
import math
def Univariate_gaussian_data_generator(mean,variance):
	S = 0.0
	while S >= 1.0 or S == 0.0:
		U = np.random.random_sample() * 2 - 1
		V = np.random.random_sample() * 2 - 1
		S = U**2 + V**2

	multiply = math.sqrt( (-2.0) * math.log(S) / S )
	U = U * multiply
	V = V * multiply

	return mean + math.sqrt(variance) * U, mean +  math.sqrt(variance) * V

def Polynomial_basis_linear_model_data_generator(basis,a,weight):
	e,_ = Univariate_gaussian_data_generator(0,a)
	x = -1.0
	while x == -1.0:
		x = np.random.random_sample() * 2 - 1
	y = 0
	for i in range(basis):
		y = y + weight[i] * x**i
	y = y + e
	return x,y

def main():
	argument = sys.argv[1:]
	if len(argument) != 3 and len(argument) != 4:
		print("You should input all the arguments")
		sys.exit(1)

	problem_class = int(argument[0])
	#Univariate gaussian data generator
	if problem_class == 0:
		mean = float(argument[1])
		variance = float(argument[2])
		X,Y = Univariate_gaussian_data_generator(mean,variance)
		print(X)
		print(Y)
	#Polynomial basis linear model data generator
	else:
		basis = int(argument[1])
		a = float(argument[2])
		s = argument[3]
		s = s.replace('[','')
		s = s.replace(']','')
		weight = []
		for i in s.split(','):
			weight.append(float(i))
		if len(weight) != basis:
			print("You should input all the arguments")
			sys.exit(1)
		x,y = Polynomial_basis_linear_model_data_generator(basis,a,weight)
		print(x)
		print(y)

if __name__ == '__main__':
	main()
