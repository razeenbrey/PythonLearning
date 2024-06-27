# Palindrome Primes.py
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 20/04/23

import sys
sys.setrecursionlimit (30000)


def main(n, m):
    
    def pn(n, i=2):
        if n == i:
            return True
        elif n % i == 0:
            return False
        return pn(n, i + 1)    
    
    if n == m+1:
        return
    if pn(n):
        if len(str(n)) == 1 or str(n) == str(n)[-1::-1]:
            print(n)
        main((n+1), m)
    if not pn(n):
        main((n+1), m)


p = int(input("Enter the starting point N:\n"))
l = int(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
main(p, l)