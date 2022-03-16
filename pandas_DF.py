import pandas as pd 
#series - one dimensional array 
#dataframe = two 
#each column in a data series 
#each key is the column and each value is each row 

grades_dict = {'Wally':[87,96,70],
                'Eva':[100,87,90],
                'Sam':[94,77,90],
                'Katie':[100,81,82],
                'Bob':[83,65,85]}

grades = pd.DataFrame(grades_dict)

grades.index = ['Test1','Test2','Test3']

print(grades)

eva = grades["Eva"]

sam = grades.Sam 


#using the loc and iloc method