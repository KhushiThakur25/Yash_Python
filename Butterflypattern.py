n = 5
'''
for i in range(1,n+1):
    for j in range(i):
        print("*",end = " ")
    for j in range(i,2*n-i):
        print(" ",end = " ")
    for j in range(2*n-i,2*n):
        print("*",end = " ")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
        print("*",end = " ")
    for j in range(i,2*n-i):
        print(" ",end = " ")
    for j in range(2*n-i,2*n):
        print("*",end = " ")
    print()
'''

for i in range(1,n+1):
    print("* "*i + "  "*(2*(n-i)) + "* "*i)
for i in range(n-1,0,-1):
    print("* "*i + "  "*(2*(n-i)) + "* "*i)










