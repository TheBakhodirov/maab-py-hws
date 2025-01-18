# 1. Write a Python program that counts the frequency of each character in a given string and prints the characters sorted by their frequency in descending order.

# 2. Write a Python program that takes a list of tuples (e.g., [(1, 2), (3, 4), (5, 6)]) and returns a new list where each tuple’s elements are swapped (e.g., [(2, 1), (4, 3), (6, 5)]).

# 3. Create a dictionary of students with their names as keys and marks as values. Write a program to find the student with the highest marks and print their name.

# 4. Write a program that takes three numbers as input and determines if they can form the sides of a triangle. If yes, classify the triangle (e.g., equilateral, isosceles, or scalene).

# 5. Write a Python program to generate the Fibonacci series up to the nth term, where n is given by the user.

# 6. Write a recursive function named power that calculates the power of a number (e.g., power(2, 3) should return 8).

# 7. Write a program that reads data from one file and writes only the lines containing the word "Python" into another file. Handle exceptions related to file operations

# -------------1-task-------------
def char_frequency(str):
    res = {}
    word = list(str)
    for char in word:
        res[char] = word.count(char)
    sorted_res = dict(sorted(res.items(),key=lambda item: item[1], reverse=True))
    return sorted_res

# print(char_frequency("Hello world"))

# -------------2-task-------------
def swap_order(ls):
    res = []
    for item in ls:
        swapped = list(item)
        swapped.reverse()
        res.append(tuple(swapped))
    return res

# print(swap_order([(1, 2), (3, 4), (5, 6)]))

# -------------3-task-------------
students = {
    "Mark": [90,86,67,88],
    "John": [89,90,68,99],
    "Nile": [95,84,79,92],
    "Sean": [78,84,86,83],
    "Liam": [64,77,80,85]
}

def highest_mark_student(ls):
    res = {}
    for item in ls.items():
        res[item[0]] = sum(item[1])
    sorted_res = sorted(res.items(), key=lambda item: item[1], reverse=True)
    return sorted_res[0][0]

# print(highest_mark_student(students))

# -------------4-task-------------
def classify_triangle():
    a = float(input("Enter side A: "))
    b = float(input("Enter side B: "))
    c = float(input("Enter side C: "))
    
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            return "Equilateral"
        elif a == b or a == c or b == c:
            return "Isosceles"
        else:
            return "Scalene"
    else:
        return "Not a valid triangle"

# print(classify_triangle())

# -------------5-task-------------
def gen_fibonacci(limit):
    a,b = 0,1
    while a < limit:
        print(a)
        a,b = b,a+b

# gen_fibonacci(10)


# -------------6-task-------------

def power(n,p):
    if p == 0: return 1
    
    return n * power(n,p-1)
        
# print(power(2,4))


# -------------7-task-------------

def filter_lines(input_file, output_file, word="Python"):
    try:
        with open(input_file, 'r') as infile:
            with open(output_file, 'w') as outfile:
                for line in infile:
                    if word in line:
                        outfile.write(line)
        print(f"Lines containing '{word}' have been written to {output_file}.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"Error: You don't have permission to read or write to one of the files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

input_file = r'hw13\input.txt' 
output_file = r'hw13\output.txt' 
filter_lines(input_file, output_file)