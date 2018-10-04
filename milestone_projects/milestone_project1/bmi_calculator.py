#To calculate the Body Mass Index

weight = float(input("Enter the weight in kg: "))

height = float(input("Enter the height in meters: "))

#BMI logic
bmi = weight/(height * height)


print("The BMI is: ", bmi)
