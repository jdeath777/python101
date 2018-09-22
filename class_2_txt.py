#day_2_class notes

#this is how we define int in python,dynamic assign
c = 0


#print the values using variables and do operations usong operators.

print(1+5)
a = 88
b = 103
print(a+b)

#using the round operators to get float 

round(0.5)
round(3.14)
print(0.6/0.2)

#mass_stone = mass_kg * 2.2/1
#mass_stone = mass_kg * 2.2/14

#using round operators to find the flooring and ceeling values
#decimal above .5 gives celling values
#decimal below .5 gives flooring values
round(-1.734)
round(-1.734,2)
round(-1.3075,2)
c = 0

#id gives the memory location of the variable 

id(c)

#assigning the three variables together seperated with , gives values to each seperately.

a,b,c = 1,"str",23
print(a)
print(b)
print(c)

#type() gives the type of the data int or string or float 
c = 1.043
type(c)

#history gives all the list of typed values in ipython
#history
#assigning different variables with the same value will
#allocate the same memory for all the variables
a = b = c =1
type(c)
id(c)
print(c)

#the del function destroys the memory form the respective variable
del c
print(c)
print(a)

#below is the list of how to do typecasting in python
#type casting changes the type of the data in the variable

float(a)
str(a)
long(a)

#below id the function to chage the string  to lower case
si = "PYTHON"
si.islower()

#below function gives the value of variable to string
str = 'programis'
print('str is = ', str)
print('str is = ',str)
print('str is =',str)
print('str is =', str)

#below list is used to get the particular letter in the string from the variable
s1 = 'python'
s1[-1]
s1[0]
s1[-6]
s1[0 : 3]
s1[-6 : -4]
s1[-6 : -3]
s1[-2 : -6]
s1[-6 : -2]
s1[-6 : 1]
s1[-6 :3 ]
s1[1 :4 ]
s1[1 :5 ]
s1[-5 : -1 ]
s1[16]
id(s1)
s1 = 'jython'
s1[0] = 'p'
del s1[0]
#using +
str1 = 'Hello'
str2 = 'World'
print("str1 + str2", str1 + str2)
print("str1 + str2 = ", str1 + str2)
print('str1 *3 = ', str1 * 3)
s1
s2 = 'python'
id(s1)
id(s2)
id(s1+" "+s2)
id(s1+s2)
name = 'jithin'
age = '24'
print("my name is {} and my age is." .format(name,age))
print("my name is %s and my age is %s." %(name,age))
print(f"my name is{name} and my age is {age}" )
