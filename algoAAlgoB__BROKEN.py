"""
NOTE: THIS SCRIPT IS BROKEN// NEEDS RE-VISITED

###- Assignment 1
Amy Brons - 20252295
Sep 24, 2022


In this assignment, two alogrithms are compared for how efficently they can search through various
data sets. The first algorithm is created to search through the set lists through linear seach. The second
algorithm searches in a binary way over the sets.
"""
import time
import random
"""
Linear search, iterating over all items of a list. This was made to be recusive. If the item
is found 'Yes' is returned, if not, 'No' is returned and else, the function calls itself.
"""
def algoA(array1, x, pos):

    # if the starting postion is correct, return yes
    if array1[pos] == x:
        return 'Yes'

    # if the item is not in the array, return no
    elif x not in array1:
        return 'No'

    # if the item has not been found, return the function
    # with a changed starting position
    else:
        return algoA(array1, x, pos+1)

    

"""
Binary search, splits a list in half and keeps splitting until the target is found.
Iterative search that calls itself.
"""
def algoB(alist, high, low, item):

    # if the top of the list and bottom have
    # not bee fully split
    if high >= low:

        # mid point declared 
        mid = (high + low)//2

        # if the mid point of the list is the item, return yes
        if alist[mid] == item:
            return "Yes"

        # if the mid point isnt the item, return the function
        # in itself, with the mid point serving as the high
        # point or low point, splitting the list again
        else:
            if item < alist[mid]:
                return algoB(alist, mid-1, low, item,)
            else:
                return algoB(alist, high,mid+1, item)

    # if not in list, return no    
    else:
        return "No"



"""
Merge sort algorithm to sort the sets into ascending order.
Parameteris only the array.
"""
def merge_sort(array):

    # This loop allows the program to avoid hitting recusion depth
    if len(array) > 1 :

        # list is recusively split into smaller and smaller pieces 
        middle = len(array)//2

        # left and right of each array is defined
        left = array[:middle]
        right = array[middle:]

        # merge sort is called recursivley on the right and left,
        # as the arrays become smaller and smaller
        merge_sort(left)
        merge_sort(right)

        # variable initialized
        i = 0
        k = 0
        j = 0

        # while the var i is less then the len of the
        # left half and the var j is less than the length of the right
        # half, loop
        while i < len(left) and j < len(right):
            if left[i] <= right[j]: # if the value of the left array is smaller
                array[k] = left[i] # define the value k as the new left item
                i +=1
            else:
                array[k] = right[j] # else define it as the new right item
                j+=1
            k+=1

        # while the left is still unsorted
        while i < len(left):
            array[k] = left[i] # define the array item as the left item
            i+=1
            k+=1 
            
        # while the right is still unsorted
        while j<len(right):
            array[k] = right[j] # define the array item as the right item
            j+=1
            k+=1




"""
Function to create sets of 10*n for the previous functions to search.
Accepts only one parameter-- the array to muliply each item by 10.
"""
def mult_10(array):   
    newlst = [] # itit a new array

    # for each item in the sorted array, multiply the item 10 times
    for i in array:
        newlst.extend([i*10])
    return newlst # return the new array of 10*n
        


"""
Function to populate a list of integers at length n. The function
only accepts n as a parameter, the length of the array.
"""
def listpop(n):
    randlist = [] # initialize list

    for i in range(n):
        # for each value in n append an integer to the
        # new list, between the values of -n and n, to
        # allow for there to be enough values for the function to choose 
        randlist.append(random.randint(-n,n))
        
    return randlist # return list

      
"""
Set variables and defined sets below. These are used in the initialization
of the functions, as well as the excution of the searches. The sets of 1000, 2000,
5000, and 10000 """

# Sets of n = 1000
n1000_rand = listpop(1000)
merge_sort(n1000_rand) # ascending order
Set1000 = mult_10(n1000_rand)

# Sets of n = 2000
n2000_rand = listpop(2000)
merge_sort(n2000_rand) # ascending order
Set2000 = mult_10(n2000_rand)

# Sets of n = 5000
n5000_rand = listpop(5000)
merge_sort(n5000_rand) # asending order
Set5000 = mult_10(n5000_rand)

# Sets of n = 10000
n10000_rand = listpop(10000)
merge_sort(n10000_rand) # ascending order
Set1000 = mult_10(n10000_rand)

# Sets of n = 16000
n16000_rand = listpop(16000)
merge_sort(n16000_rand) # asceding order
n16000 = mult_10(n16000_rand)



"""
The following set of functions are constructed to find the k* value, or the min value where Algorithm B becomes
preferable to A, given the time of each.
"""
def findk1000(k):

    # using time, we can time the length of A
    lineartime = time.time()
    algoA(Set1000, 5141768, 0 ) # in this case, we use a value in the set
    algoA(Set1000, 100, 0 ) # in this case, we use a vlue not in the set
    linearend = time.time()
    lineartimetaken = linearend-lineartime # full time taken to complete

    # using time, we can time the length of A
    binarytime = time.time()
    algoB(Set1000, len(Set1000), 0+k , 5141768) # adding k to low
    algoB(Set1000, len(Set1000), 0+k , 100)
    binaryend = time.time()
    binarytimetaken = binaryend-binarytime


    # if the binary search time is greater than or equal to the linear time, loop
    if binarytimetaken >= lineartimetaken:
        k =+1 # add one to k to iterate up the list
        return findk1000(k)

    # if time is lower than linear, loop
    elif binarytimetaken < lineartimetaken:
        return k # return k, min  value that k* is correct


"""
Same function for 2000 set. 
"""
def findk2000(k):
    
    # using time, we can time the length of A
    lineartime = time.time()
    algoA(Set2000, 24040238, 0)
    algoA(Set2000, 100, 0)
    linearend = time.time()
    lineartimetaken = linearend-lineartime # full time taken to complete
    
    # using time, we can time the length of A
    binarytime = time.time()
    algoB(Set2000, len(Set2000), 0+k , 24040238) # adding k to low
    algoB(Set2000, len(Set2000), 0+k , 100)
    binaryend = time.time()
    binarytimetaken = binaryend-binarytime


    # if the binary search time is greater than or equal to the linear time, loop
    if binarytimetaken >= lineartimetaken:
        k =+1 # add one to k to iterate up the list
        return findk2000(k)
    
    # if time is lower than linear, loop
    elif binarytimetaken < lineartimetaken:
        return k # return k, min  value that k* is correct


"""
Same function for 5000 set. 
"""
def findk5000(k):
    
    # using time, we can time the length of A
    lineartime = time.time()
    algoA(Set5000, 999958270, 0)
    lgoA(Set5000, 100, 0)
    linearend = time.time()
    lineartimetaken = linearend-lineartime # full time taken to complete
    
    # using time, we can time the length of A
    binarytime = time.time()
    algoB(Set5000, len(Set5000), 0+k , 999958270) # adding k to low
    algoB(Set5000, len(Set5000), 0+k , 100)
    binaryend = time.time()
    binarytimetaken = binaryend-binarytime

    # if the binary search time is greater than or equal to the linear time, loop
    if binarytimetaken >= lineartimetaken:
        k =+1 # add one to k to iterate up the list
        return findk5000(k)

    # if time is lower than linear, loop
    elif binarytimetaken < lineartimetaken:
        return k # return k, min  value that k* is correct


"""
Same function for 5000 set. 
"""
def findk10000(k):

    # using time, we can time the length of A
    lineartime = time.time()
    algoA(Set10000, 112646141, 0)
    algoA(Set10000, 100, 0)
    linearend = time.time()
    lineartimetaken = linearend-lineartime # full time taken to complete
    
    # using time, we can time the length of A
    binarytime = time.time()
    algoB(Set10000, len(Set10000), 0+k , 112646141)
    algoB(Set10000, len(Set10000), 0+k , 100) # adding k to low
    binaryend = time.time()
    binarytimetaken = binaryend-binarytime

    # if the binary search time is greater than or equal to the linear time, loop
    if binarytimetaken >= lineartimetaken:
        k =+1 # add one to k to iterate up the list
        return findk10000(k)

    # if time is lower than linear, loop
    elif binarytimetaken < lineartimetaken:
        return k # return k, min  value that k* is correct


"""
Print statements to figure out k* value per n value.
"""
    
print("For n = 1000, k = ", findk1000(int(0)))
print("For n = 2000, k = ", findk2000(int(0)))
print("For n = 5000, k = ", findk5000(int(0)))
print("For n = 10000, k = ", findk10000(int(0)))
        
