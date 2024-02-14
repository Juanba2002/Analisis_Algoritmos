from collections import defaultdict
def problem_1(n):
    sum=0
    for i in range(1,n):
        if i%3==0 or i%5==0:
            sum+=i
    return sum
def problem_2(n):
    a = 0
    b = 1
    c = a + b
    total = 0  
    while c < n:
        if c % 2 == 0:
            total += c
        a = b
        b = c
        c = a + b
    return total

def problem_3(n):
    i = 2
    while i * i <= n:
        while n % i == 0:
            n //= i
        i += 1
    return n
def problem_4():
    def es_palindromo(n):
        return str(n) == str(n)[::-1]

    largest_palindrome = 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if es_palindromo(product) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome
def problem_5(n):
    num = 2520
    while True:
        divisible = True
        for i in range(1, n + 1):
            if num % i != 0:
                divisible = False
                break
        if divisible:
            return num
        num += 1

print("Problem 1 Solution: ",problem_1(1000))
print("Problem 2 Solution: ",problem_2(10))
print("Problem 3 Solution: ",problem_3(13195))
print("Problem 4 Solution: ",problem_4())
print("Problem 5 Solution: ",problem_5(10))