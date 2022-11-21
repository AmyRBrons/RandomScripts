# This program imports and analyizes a set of data from a csv
# and returns the data as requested by the user. In this particular
# module there are two functions. One function establishes the data set,
# and the  second function is the main function. This deleivers a menu
# and requests user input, to determine which module, function, and data to deliver.

# Amy Brons 20252295
# CISC ###


import csv # import csv module to help read the csv dataset
import displaymod # import module
import sortandsearch # import module



"""
The following function databaseDefine reads the csv dataset.csv and returns it
at a list of dictionaries. This function takes no parameters, and calls the data
in-function. 
"""

def databaseDefine():
    # open the csv in read function
    with open('dataset.csv', mode = 'r') as data:
        dataset = [{i: n for i,n in row.items()}
                    for row in csv.DictReader(data, skipinitialspce=True)] # define the dictionary rows
        return dataset


"""
This main() function runs a gambit of test cases to ensure all modules and functions
are working correctly
"""
def main():

    # All possible displaymod test cases are shown here through unit testing

    # The first function 'displayInfo is tested all possible ways
    print(displaymod.displayInfo(10001)) # valid input
    print(displaymod.displayInfo(ADCD)) # vnvalid input

    # This uniqueDistricts function is tested through valid and invalid inputs
    print(displaymod.uniqueDistricts("Alberta"))
    print(displaymod.uniqueDistricts("England"))

    # Tests for valid and invalid cases of findMax, plus test for different keys
    print(displaymod.findMax("Electoral District"))
    print(displaymod.findMax("ValidBallots"))
    print(displaymod.findMax("Fundy Royal")) # invalid key, but still exists in data
    print(displaymod.findMax("Cucumber"))

    # Tests for valid and invalid cases of findMin, plus test for different keys
    print(displaymod.findMin("Electoral District"))
    print(displaymod.findMin("ValidBallots"))
    print(displaymod.findMin("Fundy Royal")) # invalid key, but still exists in data
    print(displaymod.findMin("Tomato"))

    # totalVotes function test cases
    print(displaymod.totalVotes(databaseDefine()))
    print(displaymod.totalVotes(title.csv))

    # Insertion sort test cases
    print(sortandsearch.insertionSort("Population", databaseDefine()))
    print(sortandsearch.insertionSort(80416, databaseDefine())) # exists in data, but invalid key
    print(sortandsearch.insertionSort("Carrot", SwissCheese))

    # Binary search test cases
    print(sortandsearch.binarySearch(13002)) # valid
    print(sortandsearch.binarySearch(59994)) # exists, but not as a valid electoral district
    print(sortandsearch.binarySearch(Dinner))
    

# run main()
main()
