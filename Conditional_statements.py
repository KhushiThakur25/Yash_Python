n = int(input("Enter your number (n)..."))
'''
if n == 30:
    print("lucky..")
'''
m = int(input("Enter your second number(m)..."))
o = int(input("Enter your third number(o)..."))
'''
if n > m:
    print(f"{n} is greater..")
else:
    print(f"{m} is greater..")
'''  
if n > m  and n > o:
    print("n is greatest..")
elif m > n and m > o:
    print("m is greatest..")
elif n == m and n == o:
    print("n,m and o are same..")
else:
    print("o is greatest..")
