# Travis Barrett
# 06/27/2024
# P2HW2
# Calculating Grade Average
num1 = float(input("Enter grade for Module 1: "))
num2 = float(input("Enter grade for Module 2: "))
num3 = float(input("Enter grade for Module 3: "))
num4 = float(input("Enter grade for Module 4: "))
num5 = float(input("Enter grade for Module 5: "))
num6 = float(input("Enter grade for Module 6: "))
print()
print(" ------------Results------------")
# Python program to find smallest 
# number in a list
 
# list of numbers
list1 = [num1,num2,num3,num4,num5,num6]
 
# sorting the list
list1.sort()
 
# printing the first element
print(f'{"Lowest Grade: ":<20}{min(list1)}')
# Python program to find largest 
# number in a list
 
# list of numbers
 
# sorting the list
print(f'{"Higest Grade: ":<20}{max(list1)}')
print(f'{"Sum of Grades: ":<20}{sum(list1)}')


print(f'{"Average: ":<20}{sum(list1)/len(list1):.2f}')


