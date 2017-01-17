def calculate(a,b, operation):
	if operation == 'add':
		return a + b
	elif operation == 'substract':
		return a - b
	elif operation == 'multiply':
		return a*b
	elif operation == 'divide':
        	return round(float(a/b),2)
	elif operation == 'greater':
		if (a < b):
			return b
		else:
			return a
	elif operation == 'smaller':
                if (a < b):
                        return a
                else:
                        return b
	elif operation == 'modulus':
                return a%b
