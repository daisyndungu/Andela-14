def find_max_min(mylist):
 for x in mylist
	max_value == max(mylist)	#finds the largest value in the list
	min_value == min(mylist)	#finds the smallest value in the list
	if min_value == max_value:	#determines whether the max value and the min values are equal
		return [len(mylist)]	#if max and min value are equal it returns the number of elements in the list
	else:				#if not it returns  a list containing both min and amx values
		return [min_value, max_value]
