# Homework1:
# 1. Create a tuple literal named cardinal_numbers that holds the strings
# "first", "second", and "third", in that order.
# 2. Using index notation and print(), display the string at index 1 in
# cardinal_numbers.
# 3. In a single line of code, unpack the values in cardinal_numbers into
# three new strings named position1, position2, and position3. Then
# print each value on a separate line.
# 4. Using tuple() and a string literal, create a tuple called my_name that
# contains the letters of your name.
# 5. Check whether the character "x" is in my_name using the in keyword.
# 6. Create a new tuple containing all but the first letter in my_name using
# slice notation.

cardinal_numbers = ("first", "second", "third")
print(cardinal_numbers[1])
(position1, position2, position3) = cardinal_numbers
print(position1)
print(position2)
print(position3)

my_name = tuple("Nodirbek")
print(my_name)

print("x" in my_name)

print(my_name[1:])

# ------------------------------------------------------------------------------
# Homework2:
# 1. Create a list named food with two elements, "rice" and "beans".
# 2. Append the string "broccoli" to food using .append().
# 3. Add the strings "bread" and "pizza" to food using .extend().
# 4. Print the first two items in the food list using print() and slice notation.
# 5. Print the last item in food using print() and index notation.
# 6. Create a list called breakfast from the string "eggs, fruit, orange
# juice" using the string .split() method.
# 7. Verify that breakfast has three items using len().
# 8. Create a new list called lengths using a list comprehension that con tains the lengths of each string in the breakfast list

food = ["rice", "beans"]
food.append("broccoli")
food.extend(["bread","pizza"])

print(food[:2])
print(food[-1])

breakfast = "eggs, fruit, orange juice".split(", ")
print(len(breakfast))

lengths = [len(x) for x in breakfast]

print(lengths)

# --------------------------------------------------------------------
# Homework3:
# Given two integer variables: a and b. Swap the values of the variables.

a = int(input("a: ")) #10
b = int(input("b: ")) #5

# You need to uncomment each option separately, one by one to check
# 1-option
# c = a
# a = b
# b = c

# 2-option
# nums = [a,b]
# b,a = nums

# 3-option
# sum = a + b
# a = sum - a
# b = sum - b

print(f"a: {a}, b: {b}")