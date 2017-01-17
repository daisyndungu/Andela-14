x= input ("Enter any number to generate Prime Numbers to: ")
if x > 1:
	for num in range(0, x):

		for factor in range(0, num):
			if (num % 2 and num % 3) == 0: #a number is said to be non prime if the number modulus 2 and 3 are both equal to zero
			 break
			else:
			 print(num) #prints prime numbers between 0->x
	else:
	 print ("Invalid output")
