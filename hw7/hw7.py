# List Comprehensions
#1. Generate a list of squares for all even numbers between 1 and 20 using a list comprehension.

#2. Create a list of strings that represent the numbers from 1 to 15, but only include numbers that are divisible by 3.

# Dictionary Comprehensions
#3. Create a dictionary where the keys are numbers from 1 to 10, and the values are the cubes of those numbers.

#4. Build a dictionary from the list ['a', 'e', 'i', 'o', 'u'] where each key is the letter, and the value is the position of the letter in the alphabet.

# Set Comprehensions
#5. Create a set of unique lengths of words from the sentence: "This is a set comprehension example in Python".

#6. Generate a set containing all the squares of numbers from 1 to 15 that are divisible by 4..

# 1-task
even_nums = [x**2 for x in range(1,21) if x % 2 == 0]
print(even_nums)

# 2-task
div_by_3 = [x for x in range(1,16) if x % 3 == 0]
print(div_by_3)

# 3-task
dict1 = {}
for x in range(1,11):
    dict1[x] = x**3
print(dict1)

dict2 = {x:x**3 for x in range(1,11)}
print(dict2)

# 4-task
letters = ['a', 'e', 'i', 'o', 'u']
letters_dict_comp = {x:ord(x.lower()) - ord('a') + 1 for x in letters}
print(letters_dict_comp)

letters_dict_loop = {}
for x in letters:
    letters_dict_loop[x] = ord(x.lower()) - ord('a') + 1
print(letters_dict_loop)

# 5-task
sentence = "This is a set comprehension example in Python"
word_length = {len(word) for word in sentence.split()}
print(word_length)

# 6-task
div_by_4 = {x**2 for x in range(1,16) if x % 4 == 0}
print(div_by_4)