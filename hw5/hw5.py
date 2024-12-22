n = int(input("Enter a number: "))

d = {}

for x in range(1,n+1):
    d.update({x: x**2})
    
print(d)

d15 = {}

for x in range(1,15):
    d15.update({x: x**2})

print(d15)