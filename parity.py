"""
Given an array A of non-negative integers, return an array consisting 
of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

iterate through the array and check if the mod of 2 is equal to 0
if it is append it to an empty array parity_array
if it is not append to another empty array odd_array
once first iteration is done append elements in odd_array to parity_array
return parity_array
"""

def parity(x):

    parity_array = []
    odd_array = []

    for num in x:
        if num % 2 == 0:
            parity_array.append(num)
        else:
            odd_array.append(num)
    
    return parity_array + odd_array

x = [6,3,5,7,9,11,2,12]
print(parity(x))         
