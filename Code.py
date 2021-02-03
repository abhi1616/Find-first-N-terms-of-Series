# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def fibo(n):
    n1 = 0
    n2 = 1
    lst = []
    lst.append(n2)
    while(True):
        next_term = n1 + n2
        if len(lst) < n:
            lst.append(next_term)
            n1 = n2
            n2 = next_term
        else:
            return lst

def primer(n):
    flag = 0
    if n < 2:
        print("Enter a valid number to check.")
    if n == 2 or n == 3:
        return 1
    for i in range(2, n):
        if (i * i) < (n + 1):
            if n % i != 0:
                flag = 1
            if n % i == 0:
                return 0
    if flag:
        return 1
    
def gene_prime(n):
    num = []
    if n == 1:
        num.append(2)
        return num
    for i in range(2, n*n):
        if (primer(i)):
            num.append(i)
        
        if len(num) == n:
            return num

def generate_series(n):
    primes = gene_prime(n)
    fibs = fibo(n)
    
    series = []
    for i in range(len(primes)):
        series.append(fibs[i])
        series.append(primes[i])
        
    return series

#driver code
if __name__ == "__main__":
    n = int(input("Enter term in series : "))
    
    if n % 2 == 0:
        print(generate_series(int(n//2)))
    else:
        print(generate_series(int(n//2) + 1)[:-1])