# 1-task
def is_prime(n):
    if (n > 0):
        for i in range(2, (n//2)+1):
            if (n % i) == 0: 
                print(False)
                break
        else: print(True)
    else: print(False)
    
# is_prime(7)

# 2-task
def digit_sum(k):
    if k < 10: return k
    return (k%10) + digit_sum(k//10)

# print(digit_sum(502))

# 3-task
def gen_powers(N):
    power = 1
    while power <= N:
        print(power, " ")
        power *= 2

# print(gen_powers(10))