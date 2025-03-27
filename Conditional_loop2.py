basic_salary = float(input("Enter your basic salary..."))

if(basic_salary <= 10000):
    HRA = 0.2 * basic_salary
    DA = 0.8 * basic_salary
    
elif(basic_salary <= 20000):
    HRA = 0.25 * basic_salary
    DA = 0.9 * basic_salary
    
else:
    HRA = 0.3 * basic_salary
    DA = 0.95 * basic_salary
    
gross_salary = basic_salary + HRA + DA

print("Your Gross salary is:",gross_salary)
