Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> li = ["amit",56,21,74,True,[1,2,3]]
>>> type(li)
<class 'list'>
>>> li[0]
'amit'
>>> li[0] = "ravi"
>>> li
['ravi', 56, 21, 74, True, [1, 2, 3]]
>>> li.append(100)
>>> li
['ravi', 56, 21, 74, True, [1, 2, 3], 100]
>>> li.append(23,45)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    li.append(23,45)
TypeError: list.append() takes exactly one argument (2 given)
>>> li.append([23,41])
>>> li
['ravi', 56, 21, 74, True, [1, 2, 3], 100, [23, 41]]
li.extend([23,41,45])
li
['ravi', 56, 21, 74, True, [1, 2, 3], 100, [23, 41], 23, 41, 45]
li.remove('ravi')
li
[56, 21, 74, True, [1, 2, 3], 100, [23, 41], 23, 41, 45]
li.remove(True)
li
[56, 21, 74, [1, 2, 3], 100, [23, 41], 23, 41, 45]
li.remove([1, 2, 3])
li
[56, 21, 74, 100, [23, 41], 23, 41, 45]
li.remove([23, 41])
li
[56, 21, 74, 100, 23, 41, 45]
li.popitem()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    li.popitem()
AttributeError: 'list' object has no attribute 'popitem'
li.pop()
45
len(li)
6
li.reverse()
li
[41, 23, 100, 74, 21, 56]
li.sort()
li
[21, 23, 41, 56, 74, 100]
li.sort(reverse = True)
li
[100, 74, 56, 41, 23, 21]
sum(li)
315
max(li)
100
min(li)
21
li
[100, 74, 56, 41, 23, 21]
m = li
m
[100, 74, 56, 41, 23, 21]
m[0]
100
m[0] = 200
m
[200, 74, 56, 41, 23, 21]
li
[200, 74, 56, 41, 23, 21]
n = li.copy()
n
[200, 74, 56, 41, 23, 21]
n[0] = 100
n
[100, 74, 56, 41, 23, 21]
li
[200, 74, 56, 41, 23, 21]
n
[100, 74, 56, 41, 23, 21]
n.clear()
n
[]
li
[200, 74, 56, 41, 23, 21]
li[0] = 100
li
[100, 74, 56, 41, 23, 21]
li.insert(0,50)
li
[50, 100, 74, 56, 41, 23, 21]
li.index(74)
2
st = "This is my python class"
st.count('s')
4
st.count('s',6)
3
st.count('s',6,21)
1
len(st)-1
22
li = [21,13,41,16,17,68,65]
large = li[0]
for i in li:
    if large < i:
        large = i

large
68
large = li[0]
second = li[0]
for i in li:
    if large < i:
        second = large
        large = i

second
41
large,second = li[0],li[0]
for i in li:
    if large < i:
        second = large
        large = i
    if i < large and i > second:
        second = i

second
65
sum = 0
for i in li:
    sum += i

sum
241
