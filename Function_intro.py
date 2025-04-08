Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def calc():
    print("Hello i'm calc")
    print("How r u..?")

    
calc()
Hello i'm calc
How r u..?
def calc(n):
    print("Value of n is:",n)
    return n

calc(5)
Value of n is: 5
5
print(calc(5))
Value of n is: 5
5
result = calc(8)
Value of n is: 8
result
8
def calc():
    print("Hello i'm calc")
    print("How r u..?")

result = calc()
Hello i'm calc
How r u..?
result
print(result)
None
def calc():
    n = 56
    m = 89
    return n+m

result = calc()
result
145
def calc(n,m):
    print("Sum of n and m is",n+m)

result = calc(2,3)
Sum of n and m is 5
result
def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return fact

result = factorial(5)
result
120
def countDigit(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

result = countDigit(123563)
result
6
def reverseNum(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n%10
        n //= 10
    return rev
... 
>>> result  = reverseNum(5632)
>>> result
2365
>>> def reverseStr(st):
...     rev = st[::-1]
...     return rev
... 
>>> if reverseStr("abbba") == "abbba":
...     print("String is palindrome")
... else:
...     print("String is not palindrome.")
... 
String is palindrome
>>> if reverseStr("abbc") == "abbc":
...     print("String is palindrome")
... else:
...     print("String is not palindrome.")
... 
String is not palindrome.
