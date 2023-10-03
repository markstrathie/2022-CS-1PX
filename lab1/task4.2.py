### Task 4 – Dictionary manipulations

#Write the following functions in Python. If you can, try to present multiple implementation for the same problem. 
#1.	`comparedicts(dict1, dict2`): Write a function that compares two dictionaries by both their keys and values and return a Boolean – loop through the dictionaries, do not simply directly compare the dictionaries with ==.

#```
#Input: {'a': 1, 'b': 2}, {'a': 1, 'b': 2}
#Output: True	

#Input: {'a': 2, 'b': 2}, {'a': 1, 'b': 2}
#Output: False


#Input: {'a': 1, 'b': 3}, {'a': 1, 'b': 2}
#Output: False
#```

#2.	`differences(dict1, dict2)`: Write a function that displays the differences between two dictionaries by returning a set of tuples.   You can assume that the dictionaries have the same set of keys.  (Extra exercise: think about how you would deal with it if they had different sets of keys?)
#```

#Input: {'a': 1, 'b': 3}, {'a': 1, 'b': 2}
#Output: {('b', 3), ('b', 2)}

#Input: {'a': 1, 'b': 3}, {'a': 1, 'b': 3}
#Output: an empty dictionary, or None
#```

keys = dict1.keys()

def comparedicts( dict1, dict2 ):
    dict1keys = []
    dict1values = []
    dict2keys = []
    dict2values = []
    for i in dict1:
        dict1keys += [i]
        dict1values += [dict1[i]]
        
    for i in dict2:
        dict2keys += [i]
        dict2values += [dict2[i]]
        
    #for i in range( len( dict1 )):
        #if dict1values[i] != dict2values[i]:
            #output += [(dict1keys[i], dict1values[i])]
            #output += [(dict2keys[i], dict2values[i])]
       
        print(dict1keys)    
        #print(dict2keys)
        #print(dict1values)
        #print(dict2values)
            
        
    #print( output )


comparedicts( {"a": 1, "b": 2}, {"a": 1, "b": 2} )
