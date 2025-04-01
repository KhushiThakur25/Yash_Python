Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(5):
...     print("*")
... 
*
*
*
*
*
>>> for i in range(5):
...     print("*",end = " ")
... 
* * * * * 
>>> for i in range(5):
...     for j in range(5):
...         print("*",end = " ")
...     print()
... 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
for i in range(5):
    for j in range(i+1):
        print("*",end = " ")
    print()

* 
* * 
* * * 
* * * * 
* * * * * 
for i in range(5):
    for j in range(5):
        print(f"{i,j}",end = " ")
    print()

(0, 0) (0, 1) (0, 2) (0, 3) (0, 4) 
(1, 0) (1, 1) (1, 2) (1, 3) (1, 4) 
(2, 0) (2, 1) (2, 2) (2, 3) (2, 4) 
(3, 0) (3, 1) (3, 2) (3, 3) (3, 4) 
(4, 0) (4, 1) (4, 2) (4, 3) (4, 4) 
for i in range(5):
    for j in range(5):
        print(i,end = " ")
    print()

0 0 0 0 0 
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
for i in range(5):
    for j in range(5):
        print(i+1,end = " ")
    print()

1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 
for i in range(1,6):
    for j in range(1,6):
        print(i,end = " ")
    print()

1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 
for i in range(5):
    for j in range(5-i):
        print("*",end = " ")
    print()

* * * * * 
* * * * 
* * * 
* * 
* 
for i in range(5):
    for j in range(i-1,5):
        print("*",end = " ")
    print()

* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
for i in range(1,6):
    for j in range(i-1,5):
        print("*",end = " ")
    print()

* * * * * 
* * * * 
* * * 
* * 
* 
n = 5
for i in range(5):
    for j in range(n-i,0,-1):
        print(j,end = " ")
    print()

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
for i in range(1,6):
    for j in range(n-i,0,-1):
        print(j,end = " ")
    print()

4 3 2 1 
3 2 1 
2 1 
1 

for i in range(5):
    for j in range(5):
        if (i == 0 or i == 4 or j == 0 or j == 4):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()

* * * * * 
*       * 
*       * 
*       * 
* * * * * 
