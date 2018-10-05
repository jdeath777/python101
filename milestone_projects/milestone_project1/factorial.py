#To find the factorial
num = int(input("Enter the number: "))

#define the fact a 1 because it cant be 0
fact = 1


#factorial of 0 is 1
if(num == 0):
    print("Factorial is 1")
else:
    for i in range(1,num+1):
        fact = fact*i
print(f"The factorial of {num} is: {fact}")
