#assigned array 
array = [11, 63, 49, 76, 47, 46, 59, 24, 45, 12]

#function for determining the range of the array, we would start from 1 as the index in 0 will be the in the sorted list or the first digit to be compared to
def insertion_sort(array):
    length = range(1, len(array))

    #function for getting every element in the array to be compared
    for i in length:
        #left value is the value in the left that would be compared to its right index
        right_value = array[i]
        #comparison while loop with swapping if the left index is greater that its right
        while array[i-1] > right_value and i>0:
            array[i], array[i-1] = array[i-1], array[i]
            i = i-1

    return array
#print output
print("Your Insertion sorted array is: ", insertion_sort(array))