# CS1PX Semester 2020/2021 
# Assessed Assignment Marking Scheme
This document at:
https://hackmd.io/@magicicada/B1K8you4d



## Specifics of tasks and mark breakdown

You should:
- choose a public dataset that is in .csv format 
    - If you find a dataset that is in, for example Excel format, it is fine to manually 'export' that to csv, and use that
- complete each of the following tasks
    
    
**Total marks possible: 75 marks**

Task A: Dataset and data structure ***(total 15 marks)***
Task A.1: **[4 marks]**
- 2 marks for properly describing the source of the data and any preprocessing done
- 2 marks for describing contents of each column including units if any


Task A.2: **[7 marks]**
- 1 point for any reasonable data structure
- 2 points for a description of the data structure
- 2 points for any reasonable justification of the data structure choice 
- 2 points for the Python example of the data structure holding some data


Task A.3: **[4 marks]**
- 1 point for each of 2 other data structure examples
- 1 point for each of 2 other justifications for non-use

Task B: Reading in your data ***(total 15 marks)***
Task B.1:  **[13 marks: 6 for functional code, 5 for error-checking, 2 for style and comments]**
- 6 points for functional code
    - 1 point for correctly taking parameter and returning value
    - 1 point for correct opening of file in Python
    - 1 point for traversing file lines with loop or similar
    - 1 point for parsing each line correctly
    - 1 point for storing values as correct type for data structure (int, string, etc)
    - 1 point for storing the information in the file in the data structure as specified in Task A
- 5 for error checking
    - 1 point for appropriate choice of defensive error-checking
    - 1 point for correct implementation of defensive error-checking
    - 2 points for correct use of try/except blocking structure
    - 1 point for dealing with caught exception (e.g. by reporting exception type with good error message, etc.)
- 2 for style and comments, 
    - 1 point for informative comments
    - 1 point for informatively named variables

Task B.2: **[2 marks]**
- 1 point for description of defensive error-checking
- 1 point for description of try/except catching

Task C: Aggregation and subsetting ***(total 20 marks)***
Task C.1: **[9 marks]**
- 5 for functional code
    - 1 point for defining function
    - 1 point for appropriate parameter and return
    - 1 point for traversal (or similar) of data structure 
    - 1 point for implementing subset condition correctly
    - 1 point for storing the selected items from the dataset in the subsetted dataset to return
- 2 for error checking
    - 1 point for choice of what to error-check (anything reasonable acceptable)
    - 1 point for correctly implementing
- 2 for style and comments, 
    - 1 point for informative comments
    - 1 point for informatively named variables


Task C.2:  **[9 marks]**
- 5 for functional code
    - 1 point for defining function
    - 1 point for appropriate parameter and return
    - 1 point for traversal (or similar) of data structure 
    - 1 point for implementing conditional of which items to include in aggregation (note: if student uses Task C.1 filter function or other helper functions this is fin - even better, really!)
    - 1 point for correctly calculating the mean/average/other aggregation
- 2 for error checking
    - 1 point for choice of what to error-check (anything reasonable acceptable)
    - 1 point for correctly implementing
- 2 for style and comments, 
    - 1 point for informative comments
    - 1 point for informatively named variables


Task C.3:  **[2 marks]**
- 1 mark for correctly identifying type or format (e.g. as another data structure, dictionary, string, list, integer, etc)
- 1 mark for any good justification

Task D: Plotting ***(total 25 marks)***
Task D.1: **[8 marks]**
- 6 for functional code
    - 1 point for correct function definition
    - 1 point for taking a parameter correctly, or other interaction with dataset 
    - 1 point for correct traversal or other interaction with data structure
    - 1 point for extraction of data for x-axis, y-axis
    - 1 point for use of .plot or .scatter function
    - 1 point for including axis labels, with units if appropriate
- 1 for code style, including informative comments
- 1 for any reasonable description of what plot shows: finding either a relationship or none is fine


Task D.2: **[8 marks]**
- 6 for functional code
    - 1 point for correct function definition
    - 1 point for taking a parameter correctly, or other interaction with dataset 
    - 1 point for correct traversal or other interaction with data structure
    - 1 point for extraction of data for histogram
    - 1 point for use of .hist function
    - 1 point for including axis labels, with units if appropriate
- 1 for code style, including informative comments
- 1 for any reasonable description of what plot shows: finding either a relationship or none is fine

Task D.3 **[9 marks]**
- 6 for functional code
    - 1 point for correct function definition
    - 1 point for taking a parameter correctly, or other interaction with dataset 
    - 1 point for correct traversal or other interaction with data structure
    - 1 point for extraction of data for histogram
    - 1 point for use of chosen function
    - 1 point for including axis labels, with units if appropriate
- 1 for code style, including informative comments
- 1 for any reasonable description of what plot shows: finding either a relationship or none is fine
- 1 for a justification of why the student has chosen that type of plot
