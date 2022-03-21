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


#using the loc and iloc methods 
test2 = grades.loc['Test2']

test1 = grades.iloc[0]

#for consecutive rows 
#when we do a colun is consecutive rows 
#when we use comma that's a nonconsecutive rows 
test1_thru_test3 = grades.loc['Test1':'Test3']
test1_and_test3 = grades.loc[['Test1','Test3']]

test1_and_test2 = grades.iloc[0:2]

#view only Eva's and Katie's grades for Test1 and Test2 
#the first part is the column and the second part is the row 
eva_katie_test1_test2 = grades.loc['Test1':'Test2',['Eva','Katie']]
#or eva_katie_test1_test2 = grades.loc[:'Test2',['Eva','Katie']]

#view only same's thru bob's grades for test 1 and test 3 
sam_thru_bob_test1_test3 = grades.loc[['Test1','Test2'],'Sam':'Bob']
# or sam_thru_bob_test1_test3 = grades.loc[['Test1','Test2'],'Sam':]
#because bob is the up-limit 

#create a data frame from everyone with a a or b grade 
grade_A_or_B = grades[(grades >= 90) | (grades >= 80)]
pd.set_option("precision",2)

print(grades.describe())

#by test 
print(grades.T.describe())

#exercise - get the average of all the students grades on each test 
print(grades.T.mean())

#sort rows by their indices (test name)
r_sorted_grades_i = grades.sort_index(ascending=False)

#sort columns by their column names (student names)
#axis = 1 indicates to sort by column indices 
#axis = 0 indicates to sort by row indices 
c_sorted_grades_i = grades.sort_index(axis = 1,ascending=False)



print()