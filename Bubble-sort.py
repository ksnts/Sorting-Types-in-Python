#assigned array 
array = [11, 63, 49, 76, 47, 46, 59, 24, 45, 12]

#function for determining the length and the -1 is for the last number which would be assumed as the biggest num in the array. 
def bubble_sort(array):
    length = len(array)-1
    #sort status for determining if the number compared is already sorted
    sortStatus = False

    while sortStatus == False :
        sortStatus = True
        #for loop for comparing 2 indexes if array i is greater than the next index then it would be sorted correctly using swap.
        for i in range (0, length):
            if array[i] > array[i+1]:
                sortStatus = False
                array[i], array[i+1] = array[i+1], array[i]

    return array
#print output
print("Your Bubble sorted array is: ", bubble_sort(array))
