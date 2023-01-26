#assigned array 
array = [11, 63, 49, 76, 47, 46, 59, 24, 45, 12]

#function for getting the length of the array 
def quick_sort(sequence):
    length = len(sequence)
    #checks if your array has more than 1 items
    if length <= 1:
        return sequence
    #pops out a value in the array which would be the pivot for quicksorting
    else:
        pivot = sequence.pop()
    #right values for the greater values than the pivot then the left values are for the items that are less than the pivot
    right_values = []
    left_values = []
    #this would put the items in the correct sorting arrays
    for number in sequence:
        if number > pivot:
            right_values.append(number)
        else:
            left_values.append(number)
    #now the pivot would be in the middle of the 2 sorted values
    return quick_sort(left_values) + [pivot] + quick_sort(right_values)

#print output
print("Your Quick sorted array is: ", quick_sort(array))

