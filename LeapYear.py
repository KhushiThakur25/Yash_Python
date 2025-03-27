year = int(input("Enter a year"))

if (year%4 == 0 and year%100 != 0)or (year%400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

'''
basic_salary = float(input("Enter your basic salary.."))
HRA = 0
DA = 0
if (basic_salary <= 10000):
    HRA = 0.2*basic_salary
    DA = 0.8*basic_salary
elif basic_salary <= 20000:
    HRA = 0.25 * basic_salary
    DA = 0.9 * basic_salary
else:
    HRA = 0.3 * basic_salary
    DA = 0.95 * basic_salary
gross_salary = basic_salary + HRA + DA

print("Your gross salary is:",gross_salary)
'''
'''
invite = "yes"
age = 19
gender = "Male"
if invite == "yes":
    print("Enter to gate number 1..")
    if age >= 18:
        print("welcome to gate number 2..")
        if gender == "Male":
            print("Welcome to party..")
        else:
            print("You are not allowed..")
    else:
        print("You are not eligible for party..")
else:
    print("Exit to gate number 1..")
'''

for i in range(2,15,2):
    print("Hello",i)









