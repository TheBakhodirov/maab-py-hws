from datetime import date

# Homework:
# 1. Create a program to ask name and year of birth from user and tell them their age.
# 2. Extract car names from this text.

#     txt = 'LMaasleitbtui'

# 3. Extract car names from this text.

#     txt = 'MsaatmiazD'

# 4. Extract residence are from this text.

#     txt = "I'am John. I am from London" 
    
    
# 1-task
name = input("What is your name? ")
year = int(input("What year were you born? "))

current_date = date.today()
current_year = current_date.year

print(f"{name}, {current_year - year} years old")

# 2-task
txt1 = 'LMaasleitbtui'
res1 = txt1[txt1.find('L')] + txt1[txt1.find('a')] + txt1[txt1.find('s')] + txt1[txt1.find('e')] + txt1[txt1.find('t')] + txt1[txt1.find('t')] + txt1[txt1.find('i')]
print(res1)

# 3-task
txt2 = 'MsaatmiazD'
res2 = txt2[txt2.find('M')] + txt2[txt2.find('a')] + txt2[txt2.find('t')] + txt2[txt2.find('i')] + txt2[txt2.find('z')]
res3 = txt2[txt2.find('D')] + txt2[txt2.find('a')] + txt2[txt2.find('m')] + txt2[txt2.find('a')] + txt2[txt2.find('z')]
print(res2)
print(res3)

# 4-task
txt3 = "I'am John. I am from London" 
residence = txt3[txt3.find("London"):]
print(residence)