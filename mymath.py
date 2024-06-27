# mymath module (used in fcombine)
# Name: Razeen
# Student Number: BRYRAZ002
# Date: 03/04/23


def get_integer (s):
   '''ensures values are digits'''
   if s == 'n':
      n = input ("Enter n:\n")
      while not n.isdigit ():
         n = input ("Enter n:\n")
      n = eval (n)
      return n
   
   elif s == 'k':
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k)
      return k

def calc_factorial (n):
   '''calculates factorials
   n - for nfactorial
   n-k - for nkfactorial'''
   if n == n:
      nfactorial = 1
      for i in range (1, n+1):
         nfactorial *= i
      return nfactorial
   if n == (n-k):
      nkfactorial = 1
      for i in range (1, n-k+1):
         nkfactorial *= i
      return nkfactorial

if __name__ == '__get_integer__':
   get_integer(s)

if __name__ == '__calc_factorial__':
   calc_factorial(n)
   
