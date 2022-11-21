"""
### -  Assignment 2
Amy Brons - 20252295

This assignment will be analyzing the time
and complexity of two different search functions
on various sets of integers. The two search
functions will be a binary seach and trinary search.

I confirm that this submission is our own work and is
consistent with the Queen's regulations on Academic Integrity.
"""

"""
Binary search function, parameters will be the
array A, the first item in the array, the last item
in the array, and the target that is being searched for.
"""
import random
import time

def bin_search(A,first,last,target):
    # returned the index of the target that is being
    # searched for if it is present in the array A
    if first > last:
        return -1
    else:
        mid = (first+last)//2 # finds the middle of the array
        if A[mid] == target:# once the list is sliced half to the target
            return mid # target is return

        # if mid hasn't been found, return function recursively
        elif A[mid] > target:
            return bin_search(A,first,mid-1,target) # adjusted last value
        else:
            return bin_search(A,mid+1,last,target) # adjusted first value



"""
Trinary search algorithm, parameters will be the
array A, the first item in the array, the last item
in the array, and the target that is being searched for.
"""
def trin_search(A,first, last, target):
    # returned the index of the target that is being
    # searched for if it is present in the array A
    if first > last:
        return -1
    else:
        # split the array into thirds
        one_third = first + (last-first)//3
        two_third = first + 2*(last-first)//3

        # if the one third split is the target, return
        if A[one_third] == target:
            return one_third
        
        # if the index of the first split is bigger than
        # the target the function is returned with an adjested
        # last point
        elif A[one_third] > target:
            return trin_search(A,first,one_third-1,target)

        # if the two third split is the target, return
        elif A[two_third] == target:
            return two_third

        # if the target is bigger than the one third, and
        # smaller than the two thirds, search the middle third
        elif A[two_third]> target:
            return trin_search(A,one_third+1,two_third-1, target)

        # if none of the previous statements apply, search the
        # highest third
        else:
            return trin_search(A,two_third+1,last,target)



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
Main function accepts no parameters, and is the function that all the
sets are created in, and experiments are run in. The both the experiment
1 and 2 are run, and an output for analyzing is output.
""" 
def main():

    # Set are created and intialized. The outcome of these lines of
    # code are to get lists of n length, random integers, sorted in
    # ascending order, where each list becomes 10*n per val.

    # Sets of n = 1000
    n1000_rand = listpop(1000)
    merge_sort(n1000_rand) # ascending order
    n1000 = mult_10(n1000_rand)

    # Sets of n = 2000
    n2000_rand = listpop(2000)
    merge_sort(n2000_rand) # ascending order
    n2000 = mult_10(n2000_rand)

    # Sets of n = 4000
    n4000_rand = listpop(4000)
    merge_sort(n4000_rand) # asending order
    n4000 = mult_10(n4000_rand)

    # Sets of n = 8000
    n8000_rand = listpop(8000)
    merge_sort(n8000_rand) # ascending order
    n8000 = mult_10(n8000_rand)
    
    # Sets of n = 16000
    n16000_rand = listpop(16000)
    merge_sort(n16000_rand) # asceding order
    n16000 = mult_10(n16000_rand)


    """
    --Experiment one--
    Analyzing binary and trinary search times with a
    target in the list.
    """

    # To make the experiments resistant to human error,
    # targets are chosen randomly. These are the targets for
    # experiment 1, where the target is in the list.
    target_in_1000 = random.choice(n1000)
    target_in_2000 = random.choice(n2000)
    target_in_4000 = random.choice(n4000)
    target_in_8000 = random.choice(n8000)
    target_in_16000 = random.choice(n16000)

    
    # Time is taken per run of the binary search, where the
    # target is in the list.
    # n=1000 time taken
    binarytime_EX1_1000 = time.time() # time started
    bin_search(n1000,0,1000,target_in_1000)
    binarytime_EX1_1000_end = time.time() # time ended
    bin_1000_Ex1 = binarytime_EX1_1000_end-binarytime_EX1_1000 # time taken

    # n=2000 time taken
    binarytime_EX1_2000 = time.time()
    bin_search(n2000,0,2000,target_in_2000)
    binarytime_EX1_2000_end = time.time()
    bin_2000_Ex1 = binarytime_EX1_2000_end-binarytime_EX1_2000

    # n=4000 time taken
    binarytime_EX1_4000 = time.time()
    bin_search(n4000,0,4000,target_in_4000)
    binarytime_EX1_4000_end = time.time()
    bin_4000_Ex1 = binarytime_EX1_4000_end-binarytime_EX1_4000

    # n=8000 time taken
    binarytime_EX1_8000 = time.time()
    bin_search(n8000,0,8000,target_in_8000)
    binarytime_EX1_8000_end = time.time()
    bin_8000_Ex1 = binarytime_EX1_8000_end-binarytime_EX1_8000

    # n=16000 time taken
    binarytime_EX1_16000 = time.time()
    bin_search(n16000,0,16000, target_in_16000)
    binarytime_EX1_16000_end = time.time()
    bin_16000_Ex1 = binarytime_EX1_16000_end-binarytime_EX1_16000

    # After getting the times taken per binary search run, outputs are mde readable
    # by suppressing scientific notation
    bin_readable_1000_ex1 = f"{bin_1000_Ex1: 8f}"
    bin_readable_2000_ex1 = f"{bin_2000_Ex1: 8f}"
    bin_readable_4000_ex1 = f"{bin_4000_Ex1: 8f}"
    bin_readable_8000_ex1 = f"{bin_8000_Ex1: 8f}"
    bin_readable_16000_ex1 = f"{bin_16000_Ex1: 8f}"
    bin_total_time_ex1 = bin_1000_Ex1+bin_2000_Ex1+bin_4000_Ex1+bin_16000_Ex1
    bin_total_ex1 = f"{bin_total_time_ex1: 8f}"

    # Experiment 1 binary search results are printed
    print("In Experiment 1, binary search results:", "\n",
          "n=1000, time:", bin_readable_1000_ex1,"\n", "n=2000, time:", bin_readable_2000_ex1,"\n",
          "n=4000, time:", bin_readable_4000_ex1,"\n", "n=8000, time:", bin_readable_8000_ex1,"\n",
          "n=16000, time:", bin_readable_16000_ex1, "\n", "Total time:",bin_total_ex1, "\n")
  

    # Time is taken per run of the trinary search, where the
    # target is in the list
    # n=1000 time taken
    trintime_EX1_1000 = time.time() # time started
    trin_search(n1000,0,1000,target_in_1000)
    trintime_EX1_1000_end = time.time() # time ended
    trin_1000_Ex1 = trintime_EX1_1000_end-trintime_EX1_1000 # time taken

    # n=2000
    trintime_EX1_2000 = time.time()
    trin_search(n2000,0,2000,target_in_2000)
    trintime_EX1_2000_end = time.time()
    trin_2000_Ex1 = trintime_EX1_2000_end-trintime_EX1_2000

    # n=4000
    trintime_EX1_4000 = time.time()
    trin_search(n4000,0,4000,target_in_4000)
    trintime_EX1_4000_end = time.time()
    trin_4000_Ex1 = trintime_EX1_4000_end-trintime_EX1_4000

    # n=8000
    trintime_EX1_8000 = time.time()
    trin_search(n8000,0,8000,target_in_8000)
    trintime_EX1_8000_end = time.time()
    trin_8000_Ex1 = trintime_EX1_8000_end-trintime_EX1_8000

    # n=16000
    trintime_EX1_16000 = time.time()
    trin_search(n16000,0,16000, target_in_16000)
    trintime_EX1_16000_end = time.time()
    trin_16000_Ex1 = trintime_EX1_16000_end-trintime_EX1_16000

    # After getting the times taken per binary search run, outputs are mde readable
    # by suppressing scientific notation
    trin_readable_1000_ex1 = f"{trin_1000_Ex1: 8f}"
    trin_readable_2000_ex1 = f"{trin_2000_Ex1: 8f}"
    trin_readable_4000_ex1 = f"{trin_4000_Ex1: 8f}"
    trin_readable_8000_ex1 = f"{trin_8000_Ex1: 8f}"
    trin_readable_16000_ex1 = f"{trin_16000_Ex1: 8f}"
    trin_total_time_ex1 = trin_1000_Ex1+trin_2000_Ex1+trin_4000_Ex1+trin_8000_Ex1+trin_16000_Ex1
    trin_total_ex1 = f"{trin_total_time_ex1: 8f}"
    
    # Experiment 1 trinary search results are printed
    print("In Experiment 1, trinary search results:", "\n",
          "n=1000, time:",  trin_readable_1000_ex1,"\n", "n=2000, time:", trin_readable_2000_ex1,"\n",
          "n=4000, time:", trin_readable_4000_ex1,"\n", "n=8000, time:", trin_readable_8000_ex1,"\n",
          "n=16000, time:", trin_readable_16000_ex1, "\n", "Total time:", trin_total_ex1, "\n")


    """
    --Experiment two--
    Analyzing binary and trinary search times, where
    the target is outside of the list.
    """

    # To make the experiments resistant to human error,
    # targets are chosen randomly. These are the targets for
    # experiment 2, where the target not in the list.
    target_out_1000 = random.choice([i for i in range(1000) if i not in n1000])
    target_out_2000 = random.choice([i for i in range(2000) if i not in n2000])
    target_out_4000 = random.choice([i for i in range(4000) if i not in n4000])
    target_out_8000 = random.choice([i for i in range(8000) if i not in n8000])
    target_out_16000 = random.choice([i for i in range(16000) if i not in n16000])


    # Time is taken per run of the binary search, where the
    # target is in the list
    # n=1000 time taken
    binarytime_EX2_1000 = time.time()
    bin_search(n1000,0,1000,target_out_1000)
    binarytime_EX2_1000_end = time.time()
    bin_1000_Ex2 = binarytime_EX2_1000_end-binarytime_EX2_1000

    # n=2000
    binarytime_EX2_2000 = time.time()
    bin_search(n2000,0,2000,target_out_2000)
    binarytime_EX2_2000_end = time.time()
    bin_2000_Ex2 = binarytime_EX2_2000_end-binarytime_EX2_2000

    # n=4000
    binarytime_EX2_4000 = time.time()
    bin_search(n4000,0,4000,target_out_4000)
    binarytime_EX2_4000_end = time.time()
    bin_4000_Ex2 = binarytime_EX2_4000_end-binarytime_EX2_4000

    # n=8000
    binarytime_EX2_8000 = time.time()
    bin_search(n8000,0,8000,target_out_8000)
    binarytime_EX2_8000_end = time.time()
    bin_8000_Ex2 = binarytime_EX2_8000_end-binarytime_EX2_8000

    # n =16000
    binarytime_EX2_16000 = time.time()
    bin_search(n16000,0,16000, target_out_16000)
    binarytime_EX2_16000_end = time.time()
    bin_16000_Ex2 = binarytime_EX2_16000_end-binarytime_EX2_16000
    

    # After getting the times taken per binary search run, outputs are mde readable
    # by suppressing scientific notation
    bin_readable_1000_ex2 = f"{bin_1000_Ex2: 8f}"
    bin_readable_2000_ex2 = f"{bin_2000_Ex2: 8f}"
    bin_readable_4000_ex2 = f"{bin_4000_Ex2: 8f}"
    bin_readable_8000_ex2 = f"{bin_8000_Ex2: 8f}"
    bin_readable_16000_ex2 = f"{bin_16000_Ex2: 8f}"
    bin_total_time_ex2 = bin_1000_Ex2+bin_2000_Ex2+bin_4000_Ex2+bin_8000_Ex2+bin_16000_Ex2
    bin_total_ex2 = f"{bin_total_time_ex2: 8f}"
    

    # Experiment 2, binary search results are printed
    print("In Experiment 2, binary search results:", "\n",
          "n=1000, time:", bin_readable_1000_ex2,"\n", "n=2000, time:", bin_readable_2000_ex2,"\n",
          "n=4000, time:", bin_readable_4000_ex2,"\n", "n=8000, time:", bin_readable_8000_ex2,"\n",
          "n=16000, time:", bin_readable_16000_ex2, "\n", "Total time:",  bin_total_ex2, "\n")

    # Time is taken per run of the binary search, where the
    # target is in the list
    # n=1000 time taken
    trintime_EX2_1000 = time.time()
    trin_search(n1000_rand,0,1000,target_out_1000)
    trintime_EX2_1000_end = time.time()
    trin_1000_Ex2 = trintime_EX2_1000_end-trintime_EX2_1000

    # n=2000
    trintime_EX2_2000 = time.time()
    trin_search(n2000,0,2000,target_out_2000)
    trintime_EX2_2000_end = time.time()
    trin_2000_Ex2 = trintime_EX2_2000_end-trintime_EX2_2000

    # n=4000
    trintime_EX2_4000 = time.time()
    trin_search(n4000,0,4000,target_out_4000)
    trintime_EX2_4000_end = time.time()
    trin_4000_Ex2 = trintime_EX2_4000_end-trintime_EX2_4000

    # n=8000
    trintime_EX2_8000 = time.time()
    trin_search(n8000,0,8000,target_out_8000)
    trintime_EX2_8000_end = time.time()
    trin_8000_Ex2 = trintime_EX2_8000_end-trintime_EX2_8000

    # n=16000
    trintime_EX2_16000 = time.time()
    trin_search(n16000,0,16000, target_out_16000)
    trintime_EX2_16000_end = time.time()
    trin_16000_Ex2 = trintime_EX2_16000_end-trintime_EX2_16000

    # After getting the times taken per binary search run, outputs are mde readable
    # by suppressing scientific notation
    trin_readable_1000_ex2 = f"{trin_1000_Ex2: 8f}"
    trin_readable_2000_ex2 = f"{trin_2000_Ex2: 8f}"
    trin_readable_4000_ex2 = f"{trin_4000_Ex2: 8f}"
    trin_readable_8000_ex2 = f"{trin_8000_Ex2: 8f}"
    trin_readable_16000_ex2 = f"{trin_16000_Ex2: 8f}"
    trin_total_time_ex2 = trin_1000_Ex2+trin_2000_Ex2+trin_4000_Ex2+trin_8000_Ex2+trin_16000_Ex2
    trin_total_ex2= f"{trin_total_time_ex2: 8f}"
    
    # Experiment 2, trinary search results are printed
    print("In Experiment 2, trinary search results:", "\n",
          "n=1000, time:", trin_readable_1000_ex2,"\n", "n=2000, time:", trin_readable_2000_ex2,"\n",
          "n=4000, time:", trin_readable_4000_ex2,"\n", "n=8000, time:", trin_readable_8000_ex2,"\n",
          "n=16000, time:", trin_readable_16000_ex2, "\n", "Total time:", trin_total_ex2, "\n")

    
main() # run
