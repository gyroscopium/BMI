# 1st input: enter height in meters e.g: 1.65
height = float(input("Enter your height in meters e.g:1.87 "))
# 2nd input: enter weight in kilograms e.g: 72
weight = int(input("Enter your weight in kilograms e.g: 90 "))
BMI = weight/(height**2)
result = round(BMI)
print("Your BMI is: " + str(result))
