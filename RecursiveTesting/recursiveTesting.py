# This program consists of a series tests for a
# my recursiveFunction module and the functions
# in it. The following module utilize the principle
# of unit testing to test normal and edge cases.

# Amy Brons 20252295
# CISC ###

import recusiveFunctions # import module to be tested


"""
This main function is constructed to run a series of
unit tests when run. 
"""
def main():

    # collapse_string tests
    print("Tests for the collapse_string function:")
    print(recusiveFunctions.collapse_string("sccchoolll")) # normal case
    print(recusiveFunctions.collapse_string("hhhhhh"))
    print(recusiveFunctions.collapse_string(" "), "\n")

    # hailstone tests
    print("Tests for the hailstone function:")
    print(recusiveFunctions.hailstone(7)) # normal case
    print(recusiveFunctions.hailstone(1))
    print(recusiveFunctions.hailstone(0), "\n")

    
    # findThree tests
    print("Tests for the findThree function:")
    print(recusiveFunctions.findThree([2,4,5,9,12,24],6, 18, count = 0)) # normal case
    print(recusiveFunctions.findThree([],0, 18, count = 0))
    print(recusiveFunctions.findThree([1,5,6], 3, 12, count = 0), "\n")

    # isReverse tests
    print("Tests for the inReverse functions:")
    print(recusiveFunctions.isReverse("hello", "olleH")) # normal case
    print(recusiveFunctions.isReverse("nope", "yeah"))
   # print(recusiveFunctions.isReverse("haha",23))
    #print(recusiveFunctions.isReverse(1,23), "\n")

    # multiplyNums tests
    print("Tests for the multiplyNums function:")
    print(recusiveFunctions.multiplyNums(10,4)) # normal case
    print(recusiveFunctions.multiplyNums(2,2))
    print(recusiveFunctions.multiplyNums(0,1), "\n")

    # searchVal tests
    print("Tests for the searchVal function:")
    print(recusiveFunctions.searchVal([[2,3],[5,6,7,8],6,[6,7]],6)) # normal case
    print(recusiveFunctions.searchVal([[],[]], 4))
    print(recusiveFunctions.searchVal([[0,0,0],0,[0,0]],0), "\n")
      

main()
