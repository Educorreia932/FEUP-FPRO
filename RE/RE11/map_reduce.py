from functools import reduce

def map_reduce(n1, n2):
	result = []
	counter = 1
	multiply = lambda a, b: a * b
	add = lambda a, b: a + b
	
	for number in range(n1, n2 + 1):    
		if number % 2 != 0:
			result.append(number ** 2)
			
	while reduce(multiply, result[0: counter]) < 50:
		counter += 1 

	if counter == 1:
		return reduce(add, result)
		
	return reduce(multiply, result[0: counter - 1]) + reduce(add, result[counter - 1:])
	