### Task 3 – Tuple manipulations

#Write the following functions in Python. If you can, try to present multiple implementations for the same problem. 
#1.	`pairTogether(list1, list2)`:  Write a function that takes two lists of the same length, and returns a new list that contains 2-tuples where the ith item in the new list is a pair composed of a 2-tuple of (ith item in list1, ith item in list2).

#```
#pairTogether([‘a’, ‘b’, ‘c’, ‘d’], [1, 2, 3, 4]) 

#output: [(a, 1), (b, 2), (c, 3), (d, 4)] 


def pairTogether( list1, list2 ):
    output = []
    for i in range( len(list1) ):
        output += [(list1[ i ], list2[ i ])]
        
    print(output)

pairTogether(["a", "b", "c", "d"], [1, 2, 3, 4])
