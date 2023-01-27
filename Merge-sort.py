#assigned array 
array = [11, 63, 49, 76, 47, 46, 59, 24, 45, 12]

def merge_sort(array):
    if len(array) > 1:
        #function into cutting the array into 2 parts mainly the left and right 
        left_values = array[:len(array)//2]
        right_values = array[len(array)//2:]
        
        #calling the function on both left and right values
        merge_sort(left_values)
        merge_sort(right_values)
        
        #x is for the left most values in left arr, y for left most element in right arr and i is for indexing 
        x = 0
        y = 0
        i = 0
        # comparison while loop for comparing left and right sub arrays
        while x < len(left_values) and y < len(right_values):
            if left_values[x] < right_values[y]:
                array[i] = left_values[x]

                x += 1
            else:
                array[i] = right_values[y]
                y += 1 
            #incrementation after comparison
            i += 1 
        #while loop for merging 
        while x < len(left_values):
            array[i] = left_values[x]
            x += 1
            i += 1 

        while y < len(right_values):
            array[i] = right_values[y]
            y += 1
            i += 1 

merge_sort(array)
#print output
print("Your Merge sorted array is: ", array)
