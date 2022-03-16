import pandas as pd 

#series is one dimentional and data frame is 2 dimensitonal 
grades = pd.Series([87,100,94])

print(grades)

a = pd.Series(98.6,range(3)) #print 98.6 three times from 0-2 

print(a)



b = grades[0]

c = grades.count()

d = grades.mean()

print(grades.describe()) # you get all the informaiton in one shot 

grades = pd.Series([87,100,94], index=['Wally','Eva','Sam'])
print(grades)

grades_dict = {'Wally':87,'Eva':100,'Sam':94}

grades_ds = pd.Series(grades_dict)

print(grades_ds)

eva = grades['Eva']
wally = grades.Wally 

e = grades.values 

hardware = pd.Series('Hammer',1,'Wrench')

f = hardware.str.contains("a")

g = hardware.str.upper()

#convert a series object to a python list 
hardware_list = hardware.to_list()

ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,10])

g = ds1 == ds2 #return true and false

ds1 > ds2 

ds1 < ds2 

#convert a series of list to one series 
list_of_series = pd.Series([
    ['Red','Green','White'],
    ['Red','Black'],
    ['Yellow']
])
#there are three elements in this list 

list_of_series = list_of_series.apply(pd.Series).stack().reset_index(drop=True)
#stack on the top of each other 

s = pd.Series(['100','200','python','300.12','400'])
sorted_series = s.sort_values()

'''
s = pd.Series(['100',200,'python',300.12,'400'])
sorted_series = s.sort_values()
#error because in double quote it's string 
#and it's can't sort if they are different data types - int and float 
'''

s.append(pd.Series(["500","php"])).reset_index(drop=True)

#write a panda program to calcualte the frequency counts of each unique value of a given series 
import random 
list1 = [random.randrange(1,10) for i in range(0,100)]
s = pd.Series(list1)

result = s.value_counts()





print()

