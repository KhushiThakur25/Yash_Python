Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = 5
>>> for i in range(n):
...     print("*",end = " ")
... 
* * * * * 
>>> for i in range(n):
...     for j in range(n):
...         if (i == 0 or i == n-1 or j == 0 or j == n-1 or i == j):
...             print("*",end = " ")
...         else:
...             print(" ",end = " ")
...     print()
... 
* * * * * 
* *     * 
*   *   * 
*     * * 
* * * * * 
for i in range(n):
    for j in range(n):
        if (i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or i == n-1-i):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()

* * * * * 
* *     * 
* * * * * 
*     * * 
* * * * * 
for i in range(n):
    for j in range(n):
        if (i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or j == n-1-i):
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()

* * * * * 
* *   * * 
*   *   * 
* *   * * 
* * * * * 
n = 5
for i in range(n):
    for j in range(i):
        print(" ",end = " ")
    for j in range(i,n):
        print("*",end = " ")
    print()

* * * * * 
  * * * * 
    * * * 
      * * 
        * 
for i in range(n):
    for j in range(n-i-1):
        print(" ",end = " ")
    for j in range(n-i-1,n):
        print("*",end = " ")
    print()

        * 
      * * 
    * * * 
  * * * * 
* * * * * 
for i in range(n):
    for j in range(n-i-1):
        print(" ",end = " ")
    for j in range(2*n+2):
        print("*",end = " ")
    print()

        * * * * * * * * * * * * 
      * * * * * * * * * * * * 
    * * * * * * * * * * * * 
  * * * * * * * * * * * * 
* * * * * * * * * * * * 
for i in range(n):
    for j in range(n-i-1):
        print(" ",end = " ")
    for j in range(n-i-1,2*n+2):
        print("*",end = " ")
    print()

        * * * * * * * * 
      * * * * * * * * * 
    * * * * * * * * * * 
  * * * * * * * * * * * 
* * * * * * * * * * * * 
for i in range(n):
    for j in range(n-i-1):
        print(" ",end = " ")
    for j in range(n-i-1,2*i+2):
        print("*",end = " ")
    print()

        
      * 
    * * * * 
  * * * * * * * 
* * * * * * * * * * 
for i in range(n):
    for j in range(n-i-1):
        print(" ",end = " ")
    for j in range(n-i-1,2*i+1):
        print("*",end = " ")
    print()

        
      
    * * * 
  * * * * * * 
* * * * * * * * * 
for i in range(4):
    for j in range(4-i-1):
        print(" ",end = " ")
    for j in range(2*i+1):
        print("*",end = " ")
    print()

      * 
    * * * 
  * * * * * 
* * * * * * * 
for i in range(n):
    for j in range(n-i-1):
        print(" ",end = " ")
    for j in range(2*i+1):
        print("*",end = " ")
    print()

        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
