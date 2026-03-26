#===============
# 6. User Input
#==============
# Ask the user for their name and greet them.
#--------------------------------------------------------
name = input("Enter your name : ")
print(f"GOOD MORNING : {name}")
# Ask the user for age and print age next year.
#--------------------------------------------------------
age = int(input("ENTER YOUR AGE : "))
print(f"YOUR AGE WILL BE NEXT YEAR : {age+1}")
#--------------------------------------------------------
# Ask the user for height in meters and print it in centimeters.
height = float(input("Enter your height in meters : "))
print(f"Height in centimeters : {height*100}")
# Ask the user for two numbers and print their sum.
num1 = int(input("ENTER THE VALUE OF NUM1 : "))
num2 = int(input("ENTER THE VALUE OF NUM2 : "))
print("-----------------------------------------------------")
print(f"SUM OF NUM1 : {num1} AND NUM2 : {num2} = {num1+num2}")
print("-----------------------------------------------------")
# Ask the user for temperature in Celsius and convert it to Fahrenheit.
temp_celsius = int(input("Enter the temperature in Celsius : "))
print(f"Temperature in Fahrenheit is : ({(temp_celsius*1.8)+32})")
