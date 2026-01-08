import math

def is_prime(n):
    if n <=1 :
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

a = [1, 88, 77, 22, 41, 9, 15]  
a_odd = [x for x in a if x % 2 != 0]
a_even = [x for x in a if x % 2 == 0]
a_prime = [x for x in a if is_prime(x)]

a_odd.sort()
a_even.sort()
a_prime.sort()


print("Oddetall = ", a_odd, "\n", "Partall =", a_even, "\n", "Primme =", a_prime)
