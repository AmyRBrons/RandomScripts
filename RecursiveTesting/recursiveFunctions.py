# This program consists of a series of recursive functions including a function
# that removes adjacent letters in a string, a function that generates
# the hailstone sequence of numbers, a function that searches a list
# to determine if three numbers will equal a sum, a function that accepts two
# strings and returns true if they are the reverse of each other, a function
# that determines the product of two numbers, and a function that accepts
# a list and finds how many times a certain value occurs in it. All functions are recursive.
# The second part of this program is the testing script, which consists of a series of
# short unit tests for the recursive functions of this program.
# The third part of this program is a block comment responding to a question posed
# for this project.

# Amy Brons 20252295
# CISC ###


"""
The collapse_string function accepts a string and uses
recursion to remove characters that repeat within the string.
The function takes in one string as a parameter.
"""
def collapse_string(myString):
    # if the string has a length of 1, then there are no
    # double characters to remove, and the string can be
    # returned as is
    # base case
    if len(myString) == 1:
        return myString # string returned

    # if the first character of the first string is not equal
    # to the second character, the function is re-ran with
    # modified parameters
    if myString[0] != myString[1]:
        # return the confirmed new character, plus the
        # function is re-ran with the string minus this character
        return myString[0] + collapse_string(myString[1:])

    # return the function with the remaining string, printing the
    # fully 'collapsed' string
    return collapse_string(myString[1:])


"""
This function returns the hailstone number sequence up to a certain
number of terms. The integer to generate the sequence from is inputted
as the parameter and this function generates the hailstrom sequence until
1 is reached.
"""
def hailstone(n):
    # error catching for zero, base case
    if n == 0:
        return []
    
    # if 1 is reached, return list of n, base case
    if n == 1:
        return [n]

    # if 1 has not been reached, loop
    else:
        # if n is even, loop
        if n % 2 == 0:
            # return a list of n, plus re-run the function
            # with half of n as the parameter
            return [n] + hailstone(n//2)
        # if n is odd, loop
        else:
            # return a list of n, plus 3 times n plus one as
            # the parameters
            return [n] + hailstone((3*n)+1)



"""
The findThree function finds if three items in a list could add
together to equal a target. The function takes in four parameters;
a list, a length of said length, a sum of the numbers, and a count
"""
# len(lis) will be put in as a variable called length, as this prevents
# possible errors
def findThree(lis, length, sum, count = 0):

        
    if length <= 3:
        # if the count is 3 and the sum is 0 return true, base case
        if count == 3 and sum == 0:
            return True
        # if count is greater than three, then there are more than three
        # values that add to the sum, therefore a False is returned
        elif count > 3:
            return False

        
        # if neither, loop
        else:
            # for each instance in the length of list
            for i in range(length):
            # if this findThree algorithm can be ran again (with changed parameters
            # to accound for the already passed items)
                return findThree(lis[:i] + lis[i+1:], length-1, sum - lis[i], count+1)

            return True
    else:
        return False
        
    

"""
The isReverse function accepts two parameters that are strings, and uses recursion to
figure out if these two strings are the reverse of each other. A boolean response is
the return value of this function.
"""
def isReverse(firstString, secondString):
    
    # if the lengths are the same, loop
    if len(firstString) == len(secondString):

        # lowercase the two strings    
        firstString = firstString.lower()
        secondString = secondString.lower()

        # base case, if both lengths are different, return true
        # as the empty strings are the reverse of each other
        if len(firstString) == 0 and len(secondString) == 0:
            return True

        # if the first character and last character of each
        # string then recursively call isReverse
        elif firstString[0] == secondString[-1]:
            return isReverse(firstString[1:], secondString[:-1])

        
        # if neither of the above is true, return false
        else:
            return False
        
    # error catch, all other cases, and string of different lengths
    else:
        return False
        
       

"""
multiplyNums accepts two interger values and recursively calculates
the product of multiplying those two values. The return value of
this function is returned.
"""    
def multiplyNums(firstVal, secondVal):

    # to order the numbers correctly for the multiplication
    # run function again with correct order
    if firstVal < secondVal:
        return multiplyNums(secondVal, firstVal)

    # else, the order is correct
    else:
        # base case, if the two values are 0, return 0
        if secondVal == 0 and firstVal == 0:
            return 0

        # if both values are not 0, recursively call the function
        # with adjusted secondVal, and add to first val. This is
        # the portion that calculates the return value
        if secondVal != 0 and secondVal != 0:
            return firstVal + multiplyNums(firstVal, secondVal-1)

        # else, error catching, and accounting for cases where one
        # value is equal to 0, which would be 0
        else:
            return 0


"""
This function accepts two parameters, a list, and a target. This function
counts how many times the target is accepted in the list. The return value
will be the number of times the target appears within the list.
"""
def searchVal(intList, target):

    # if the list is empty, return 0, base case
    if intList == []:
        return 0

    # if there are lists in the list, loop
    if type(intList[0]) == type([]):
        # return the function  within that list in list
        return searchVal(intList[0], target) + searchVal(intList[1:], target)

    # for all non list items that are populated
    else:
        # if the list item is the target, loop
        if intList[0] == target:
            # return 1, and add the recursive function on this, to check the rest of list
            return 1 + searchVal(intList[1:], target)

        # else, return 0 and check the rest of list by recursively calling function
        else:
            return 0 + searchVal(intList[1:], target)


"""
This main function is constructed to run a series of
unit tests when run. 
"""
def main():

    # collapse_string tests
    print("Tests for the collapse_string function:")
    print(collapse_string("sccchoolll")) # normal case
    print(collapse_string("hhhhhh"))
    print(collapse_string(" "), "\n")

    # hailstone tests
    print("Tests for the hailstone function:")
    print(hailstone(7)) # normal case
    print(hailstone(1))
    print(hailstone(0), "\n")

    
    # findThree tests
    print("Tests for the findThree function:")
    print(findThree([2,4,5,9,12,24],6, 18, count = 0)) # normal case
    print(findThree([],0, 18, count = 0))
    print(findThree([1,5,6], 3, 12, count = 0), "\n")

    # isReverse tests
    print("Tests for the inReverse functions:")
    print(isReverse("hello", "olleH")) # normal case
    print(isReverse("nope", "yeah"))
    print(isReverse("23","32"))
    print(isReverse("1","11"), "\n")

    # multiplyNums tests
    print("Tests for the multiplyNums function:")
    print(multiplyNums(10,4)) # normal case
    print(multiplyNums(2,2))
    print(multiplyNums(0,1), "\n")

    # searchVal tests
    print("Tests for the searchVal function:")
    print(searchVal([[2,3],[5,6,7,8],6,[6,7]],6)) # normal case
    print(searchVal([[],[]], 4))
    print(searchVal([[0,0,0],0,[0,0]],0), "\n")
      

main()


"""
Question 7 - Part 3 - Computational Complexity

For this question, we have been asked to find the computational
completity of this function. To find this, we must consider the
value of n (in this case lis) to be the factor in which the time
of the function grows. I have commented on the below formula how I
came to my solution.

def mystery(lis):

    n = len(lis)

    for index in range(n): # a for loop for range(n) gives the O(n) complexity

        # given that this is somewhat negligable, as it does grow per growth on
        # n, this particular internal info can be discounted when calculating big O
        x = 2*index % n 

        lis[index],lis[x] = lis[x],lis[index]

    print(lis)


Given that the loops worst case is O(n), and the internal info is
negligable, the complexity is O(n).

"""
