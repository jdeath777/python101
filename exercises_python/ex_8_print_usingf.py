#print using the f statement

different_people = 10

x = f"There are {different_people} types of people."

binary = "binary"

do_not = "don't"

y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said : {y}")

funny = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(funny))

w = "This is the left side of..."
e = "This is the right side of string."

print(w+e)
