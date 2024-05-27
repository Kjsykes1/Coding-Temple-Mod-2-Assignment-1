#Task 1 Identify the Greatest

number_1 = 5
number_2 = 5
number_3 = 11 

#number_1 = float(input("Enter first number: "))
#number_2 = float(input("Enter second number: "))
#number_3 = float(input("Enter third number: "))
if (number_1 >= number_2) and (number_1 >= number_3):
    largest = number_1
elif (number_2 >= number_1) and (number_2 >= number_3):
    largest = number_2
else: 
    largest = number_3
print("The largest number is", largest)

#Task 2 Identify the Smallest
#number_1 = float(input("Enter first number: "))
#number_2 = float(input("Enter second number: "))
#number_3 = float(input("Enter third number: "))

if (number_1 <= number_2) and (number_1 <= number_3):
    smallest = number_1
elif (number_2 <= number_1) and (number_2 <= number_3):
    smallest = number_2
else: 
    smallest = number_3
print("The smallest number is", smallest)

#Task 3 Equality Check

if (number_1 == number_2) and (number_1 == number_3):
    "Two numbers are equal and the largest is"
else:
    (number_1, number_2, number_3)
print("Two numbers are equal and the largest is", number_3)