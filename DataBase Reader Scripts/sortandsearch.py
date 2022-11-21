# This program imports and analyizes a set of data from a csv
# and returns the data as requested by the user. In this particular
# module there are two functions relating to searching and sorting.
# The first function is an intertion sort, and the second is a binary search.

# Amy Brons 20252295
# CISC ###

import databaseReader # import data
import displaymod # importfunctions
"""
The insertionSort function takes in a set of data and a key, and
sorts the data from lowest to highest value, inplace. This is an example
of a typical insertion sort in it's construction.
"""
def intertionSort(key,data):

    # if the key is in the data set, loop
    if key in data:
        # for all items in the length of data
        for i in range(0, len(data)):
            # define where the key is
            key = data[i]
            # set a variable to run through the insertion
            # sort and derive a position from
            n = i -1 # initialized as just under the key
            # while the variable is greater or equal to zero,
            # and the key is less than the variable defined spot
            # in data, loop
            while n >= 0 and key < data[n]:
                # reposition the search place as n+1
                data[n+1] = data[n]
                # subtract one from the search variable
                n -= 1
            # once the loop finishes, it can be known that
            # the key is one more spot in data than the variable
            # location
            data[n+1] = key

    # error catching        
    else:
        print("This is not a valid key.")


"""
This binary search function acts as a typical binary seach would,
and looks for an electoral district based on it's electoral district
number.
"""
def binarySearch(electNum):
    # define the data set
    data = databaseReader.databaseDefine()

    # if the parameter is in the data, loop
    if electNum in data:

        # low to high, low and high values can be set as so
        low == displaymod.findMin("Electoral District Number")
        high == displaymod.findMax("Electoral District Number")

        # mid value can be found through adding together and
        # dividing
        mid = (low + high)//2

        # if the electNum parameter is larger than the mid point
        # the new high number is set as one above the mid point
        if electNum > mid:
            high = mid + 1
            
        # if the electNum parameter is smaller than the mid point
        # the new low number is set as one below the mid point
        elif electNum < mid:
            low = mid - 1

        # if the mid point is equal to the param, return the mid
        else:
            return mid

    # error catching
    else:
        print("Sorry, there was an error.")
