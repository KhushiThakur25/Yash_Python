n = int(input("Enter the values for check whether it is prime or not.."))
'''
for i in range(2,n):
    if (n%i == 0):
        print("Number is not prime..")
        break
else:
    print("Number is prime..")
'''

'''
prime = True
for i in range(2,n):
    if (n%i == 0):
        print("Number is not prime..")
        prime = False
        break
if prime:
    print("Number is prime..")
'''

first = 0
second = 1
print(first,second,end = " ")
for i in range(2,n):
    third = first + second
    print(third,end= " ")
    first = second
    second = third
