def find_missing(arr1, arr2):
    new_list = []
    for element in arr1:
        if element not in arr2:
            new_list.append(element)
    for element in arr2:
        if element not in arr1:
            new_list.append(element)

    if len(new_array) > 0:
        if len(new_array) == 1:
            return new_array[0]
        else:
            return new_array
    else:
        return 0
    
