import math
def isPrime(num):
    for i in range(int(math.sqrt(num))):
        if (num % i == 0): return False
    return True



