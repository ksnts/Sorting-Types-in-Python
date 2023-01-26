#assigned array 
array = [11, 63, 49, 76, 47, 46, 59, 24, 45, 12]

#function for getting the length of the array
def selection_sort(array):  
    length = len(array)  
    
    #we are declaring our min index which would when we swap to a lower value, -1 is there for it to declare if there is only 1 digit left it is assumed as the biggest num
    for i in range(length-1):  
        minIndex = i  
          
        #this is the scanning part where it compares the next number to the minimum
        for j in range(i+1, length):  
            if array[j]<array[minIndex]:  
                minIndex = j  

        #swapping the min with the lower value index          
        array[i], array[minIndex] = array[minIndex], array[i]

    return array
#print output
print("Your Selection sorted array is: ", selection_sort(array))