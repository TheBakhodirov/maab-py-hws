# 1-task
# find a leap year
year = int(input("Input the year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# 2-task
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird

n = int(input("Enter the number: "))

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0:
    if n in range(2,6) or n > 20:
        print("Not weird")
    elif n in range(6,21):
        print("Weird")

# 3-task Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop. 
# Give two solutions.
# Solution 1 with if-else statement.
# Solution 2 without if-else statement.

# 1
a = int(input("A: "))
b = int(input("B: "))

if a % 2 != 0:
    a += a % 2

if a % 2 == 0:
    even_nums = range(a,b+1,2)
    print(*even_nums)
    
# 2
a = int(input("A: "))
b = int(input("B: "))

a += (a % 2)

e_nums = list(range(a,b+1,2))
print(e_nums)  