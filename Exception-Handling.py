
try:
    a = int(input("Enter the value 1"))
    b = int(input("Enter the value 2"))
    add = a + b
    sub = a-b
    mul = a*b
    div = a/b
except ZeroDivisionError as msg:
    print("Int can't be divide by zero..")
except ValueError as msg:
    print(msg)
except Exception as msg:
    print(msg)
else:
    print(add)
    print(sub)
    print(mul)
    print(div)
finally:
    print("Thanks for visiting.....")


'''
def atm():
    pin = "1234"
    total = 10000
    PIN = input("Enter your pin: ")
    if PIN == pin:
        print("Login Successfully..")
    else:
        raise ValueError("Login Failed..")
    amount = int(input("Enter the amount.."))
    
    if amount > total:
        raise ValueError("Insufficient Balance")
    else:
        remaining = total-amount
    print("Your current balance is:",remaining)

try:
    atm()
    #user-defined error
except ValueError as msg:
    print(msg)
    #system-defined error
except Exception  as msg:
    print(msg)

'''













