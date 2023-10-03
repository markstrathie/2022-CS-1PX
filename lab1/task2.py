### Task 2 – List manipulations

#Write the following functions in Python. If you can, try to present multiple implementation for the same problem. 
#1.	`howManyZeroes(a)`: Write a function that counts the number of entries in list a that are equal to the number 0
#2.	`getTheOddNumbers(a)`: Write a function that returns a list containing only the odd-number entries of a list.

count = 0
list1 = [ 1, 2, 0, 3, "eggs", 0, "chicken", 0, 999999 ]

for i in list1:
    if i == 0:
        count += 1

print (count)
