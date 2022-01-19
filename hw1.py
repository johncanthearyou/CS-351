#CS351 -- HW1
#John Stockton
#Winter 2022

# Precondition: len(nums1) == len(nums2) and nums1 != []
# Input: (list of number, list of number) -> number
# Output: Greatest absolute difference between numbers at corresponding
#         positions in nums1 and nums2.
def greatest_difference(nums1, nums2):
    if( len(nums1)==0 | len(nums1)!=len(nums2) ): return -1

    maxDiff = 0
    currDiff = maxDiff
    for idx in range( len(nums1) ):
        currDiff = abs( nums1[idx]-nums2[idx] )
        maxDiff = maxDiff if ( currDiff<=maxDiff ) else currDiff
    return maxDiff


#Input: (list of int, int) -> bool
#Output: True if and only if it is possible to form amount, which is a 
#        number of cents, using exactly two coins, which can be of any 
#        of the denominations in denoms.
def can_pay_with_two_coins(denoms, amount):
    i=0
    while( i<len(denoms) ):
        j=i
        while( j<len(denoms) ):
            if( denoms[i]+denoms[j] == amount ): return True
            j += 1
        i += 1
    #If we get here, we tried all combos and nothing worked, return false
    return False


#Input: (str) -> bool
#Output: True if every letter in s is fluffy. Fluffy letters are those that
#        appear in the word 'fluffy'.
def all_fluffy(s):
    fluffyLetters = "fluy"
    for idx in range( len(s) ):
        if( fluffyLetters.find(s[idx])==-1 ): return False
    return True


#Precondition: s.isdigit() holds for each string s in nums_list.
#Input: (list of str) -> int
#Output: the sum of all the digits in all strings in nums_list.
def digital_sum(nums_list):
    total = 0
    for i in range( len(nums_list) ):
        for j in range( len(nums_list[i]) ):
            total += int( nums_list[i][j] ) #Read char value as int
    return total
    

#Input: (int) -> int
#Output: the number of steps it takes to reach 1, by applying the two steps
#        of the Collatz conjecture beginning from n.
def count_collatz_steps(n):
    numSteps = 0

    while(n!=1):
        if(n%2==0): n /= 2
        else: n = 3*n + 1
        numSteps += 1

    return numSteps