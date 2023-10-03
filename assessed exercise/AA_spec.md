# CS1PX Semester 2021/2022 - Assessed Assignment

- Worth 20% of course grade
- Released before March 1st
- Due: 25th March

### Outline
For this assignment, you will find a public dataset that you find interesting and produce Python code that reads in this data, stores it in a custom data structure, aggregates and subsets the data, and plots characteristics of the data using `matplotlib`.

You should read through the specifics of the assignment requirements *before* choosing your dataset to make sure you choose one that allows you to complete all the parts of this assignment.  For example, you will need something that allows the kinds of plot required.  If you don't know where to start looking for data, you could start with public datasets on: https://www.kaggle.com/datasets, https://data.gov.uk/.

If you are working with a dataset and there are a small number of lines that contain strings you cannot parse using the techniques we've used in CS1PX (e.g. they have commas in the middle of values) then you should adapt your code to ignore these lines.  

You will be marked on your code (including style and error-checking), as well as your text describing what you have done and the coding choices you have made. 


## Specifics of tasks and mark breakdown

You should:
- choose a public dataset that is in .csv format 
    - If you find a dataset that is in, for example Excel format, it is fine to manually 'export' that to csv, and use that
- complete each of the following tasks
    
    
**Total marks possible: 75 marks**

Task A: Dataset and data structure ***(total 15 marks)***
1. describe your dataset in words, saying where you got it and what each of the columns means
    - **[4 marks]**
2. design a data structure to hold the information in your dataset, and justify your choice of data structure. Include an Python example of your data structure on a small example of your data. 
    - **[7 marks]**
3. describe two other options for possible data structures, and say why they are not as good as the one that you chose
    - **[4 marks]**

Additional notes on your data structure choice: If you chose a dataset with a very large number of columns you may want to disregard some of them.  In this case, you may discard some before you process the data in Python, then explain in the Task 1A where you got the data, why you kept the columns you did, and which columns you discarded.  You then don't need to explain the contents of the columns you have discarded. 





Task B: Reading in your data ***(total 15 marks)***
1. write a function called `read_data(filename)` that takes your .csv `filename` as an argument, and `returns` an instance of the data structure you have devised.  You should use at least one example of defensive error-checking and one example of exception-catching.
    - **[13 marks: 6 for functional code, 5 for error-checking, 2 for style and comments]**
3. describe in words what error-checking you have chosen and why.
    - **[2 marks]**





Task C: Aggregation and subsetting ***(total 20 marks)***
1. choose a characteristic of your data to filter (or subset) by, and write a function that takes as arguments the data structure and the specification of the characteristic and `returns` a subset of the data structure containing records that meet that characteristic:  similar to, for example `filterByRegion(dataStruct, regionString)` from our lab in Cycle 4.  Your function should be called `filter_by_characteristic`.
    - **[9 marks: 5 for functional code, 2 for error-checking, 2 for style and comments]**
2. choose a characteristic of your data to aggregate by, and write a function that finds mean values of a numeric value of your data by that characteristic (similar to, for example, finding the mean price per unit for each month in the lab in Cycle 4), and `returns` this information in some format that you choose. Your function should be called `aggregate_by_characteristic`
    - **[9 marks: 5 for functional code, 2 for error-checking, 2 for style and comments]**
3. Describe in words why you chose the format you did as a return valie for C.2 (e.g. why a dictionary, or data structure, or list, etc.).
    - **[2 marks]**





Task D: Plotting ***(total 25 marks)***
1. Choosing an appropriate characteristic of your data to show, define a function to visualise that characteristic using either `.scatter` or `.plot` from `matplotlib`. Describe in words what your plot shows in terms of your data - that is, *do not* just say 'this shows a scatter plot of my data', but instead something about the relationship or lack of relationship in your data.
    - **[8 marks: 6 for functional code including axis labels, 1 for code style, 1 for description]**
2. Choosing an appropriate characteristic of your data to show, define a function to visualise a histogram of that characteristic using `.hist` from `matplotlib`. Describe in words what your plot shows.
    - **[8 marks: 6 for functional code including axis labels, 1 for code style, 1 for description]**
2. Choosing an appropriate characteristic of your data to show, define a function to visualise that characteristic using some plot style other than plain plotting, scatterplot, or histogram from `matplotlib`. Describe in words what your plot shows and why you chose that style.
    - **[9 marks: 6 for functional code including axis labels, 1 for code style, 2 for description]**





### What you should submit

You may submit either:
- a Jupyter notebook (I suggest this one with code and text additions) that contains your written descriptions and code, along with your .csv file, or
- a .py Python file containing your code and the clearly-labelled written parts as comments, and your .csv file.

Do not submit any file with an extension other than .py, .ipynb, or .csv  
- Please do not submit text files
- Please do not submit Word files
- Please do not submit Excel files
- Please do not submit pdf files
- Please do not submit html files


