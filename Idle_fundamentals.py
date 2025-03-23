Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello world")
Hello world
>>> n = 5
>>> print("n")
n
>>> print(n)
5
>>> import keyword
>>> print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> True = "siya"
SyntaxError: cannot assign to True
>>> name = "Riya"
>>> Name = "siya"
name
'Riya'
Name
'siya'
5name = "om"
SyntaxError: invalid decimal literal
_age = 56
st = {1,1,2,3}
len(st)
3
st
{1, 2, 3}
st = {"om","om",1,1,1,2,2,3,5,6,7}
len(st)
7
st
{1, 2, 3, 5, 6, 7, 'om'}
li = [1,5,2,4,3,1]
li[0]
1
li[0] = 100
li
[100, 5, 2, 4, 3, 1]
tup = (1,2,5,63,1,4)
tup[0]
1
tup[0] = 100
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tup[0] = 100
TypeError: 'tuple' object does not support item assignment
del tup[0]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    del tup[0]
TypeError: 'tuple' object doesn't support item deletion
type(tup)
<class 'tuple'>
a = 5
b = 2
x = 56
y = 32
a + b
7
print(a - b)
3
print(a * b)
10
print(a/b)
2.5
print(a//b)
2
print(a%b)
1
print(a**b)
25
print(x == y)
False
print(x != y)
True
print(x < y)
False
print(x > y)
True
#print(a-b)
print("Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.")
      
SyntaxError: unterminated string literal (detected at line 1)
print("""Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.""")
      
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.
'''When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.'''
      
'When the blazing sun is gone,\nWhen he nothing shines upon,\nThen you show your little light,\nTwinkle, twinkle, all the night.'
