#print statements in different lines  

#declareing the variable
days = "Mon Tue Wed Thu Fri Sat Sun" 

#declaring the variable in new lines
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("input: days \nmonths")

print("""
excepted output: 
Here are the days: Mon Tue Wed Thu Fri Sat Sun
Here are the months: Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug
""")

print("Actuall output")
print("Here are the days: ", days)  

print("Here are the months: ", months)

print(""" 
There's something going on here.With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6. 
""")
