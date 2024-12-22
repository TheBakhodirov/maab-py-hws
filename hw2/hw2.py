# Homework:

# Given a side of square. Find its perimeter and area.
# Given diameter of circle. Find its length.
# Given two numbers a and b. Find their mean.
# Given two numbers a and b. Find their sum, product and square of each number.

#1-task
a = int(input("Enter the side of the square: "))
P = 4 * a
A = a ** 2
print(f"The perimeter is: {P} and area is: {A}")

# 2-task
d = int(input("Enter the diameter of the circle: "))
C = 3.14 * d
print(f"The length of the circle is: {C}")

# 3-task
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
M = (n1 + n2) / 2;
print(f"The mean is: {M}")

# 4-task
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
summ = num1 + num2
product = num1 * num2
sqr1 = num1 ** 2
sqr2 = num2 ** 2
print(f"Sum: {summ}, Product: {product}, Square1: {sqr1}, Square2: {sqr2}")