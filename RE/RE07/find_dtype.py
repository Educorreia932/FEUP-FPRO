def find_dtype(atuple, data_type):
	result = ()

	for element in atuple:
		if data_type == type(element).__name__:
			result += (element,)

	return result
