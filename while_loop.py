'''i = 0
while i < 10:
    print("Hello user",i)
    i += 1'''
n = int(input("Enter the value.."))
'''
count = 0
while n > 0:
    count += 1
    n //= 10
print("Your digit count is:",count)
'''
org = n
rev = 0
while n > 0:
    rev = rev * 10 + n%10
    n //= 10
print("Your reverse number is :",rev)

if org == rev:
    print("Number is palindrome..")
else:
    print("Number is not palindrome..")
