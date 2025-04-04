Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> li = [2,15,3,4,81,5,3,6]
>>> leader = True
>>> for i in range(len(li)-1):
...     leader = True
...     for j in range(i+1,len(li)):
...         if li[i] < li[j]:
...             leader = False
...             break
...     if(leader):
...         print(li[i])
... 
81
>>> print(li[len(li)-1])
6
>>> leader = 0
>>> for i in range(len(li)-1,-1,-1):
...     if leader > li[i]:
...         print(leader)

for i in range(len(li)-1,-1,-1):
    if leader < li[i]:
        print(leader)

0
0
0
0
0
0
0
0
for i in range(len(li)-1,-1,-1):
    if leader < li[i]:
        leader = li[i]
        print(leader)

6
81
tu = 2,1,45,2,12,36,4
type(tu)
<class 'tuple'>
tup = (1,2,4,5,8,7,9,3,6)
type(tup)
<class 'tuple'>
sum(tup)
45
max(tup)
9
min(tup)
1
tup.count(5)
1
len(tup)
9
tup[0]
1
tup[0] 3
SyntaxError: invalid syntax
tup[0] = 3
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    tup[0] = 3
TypeError: 'tuple' object does not support item assignment
tup.index(5)
3
tup.clear()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    tup.clear()
AttributeError: 'tuple' object has no attribute 'clear'
del tup
tup
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    tup
NameError: name 'tup' is not defined. Did you mean: 'tu'?
tu
(2, 1, 45, 2, 12, 36, 4)
tu[1]
1
tu[1] = 100
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    tu[1] = 100
TypeError: 'tuple' object does not support item assignment
tu = list(tu)
type(tu)
<class 'list'>
tu[1]
1
tu[1] = 100
tu
[2, 100, 45, 2, 12, 36, 4]
tu = tuple(tu)
tu
(2, 100, 45, 2, 12, 36, 4)
st = {}
type(st)
<class 'dict'>
st = set()
st
set()
type(st)
<class 'set'>
st = {1,2,3,4,5}
sts = {4,5,6,7,8}
st.union(sts)
{1, 2, 3, 4, 5, 6, 7, 8}
t = {1,11,2,1,2,1,2,12}
len(t)
4
t
{1, 2, 11, 12}
st.intersection(sts)
{4, 5}
st
{1, 2, 3, 4, 5}
st.update(sts)
st
{1, 2, 3, 4, 5, 6, 7, 8}
st = {1,2,3,4,5}
st.intersection_update(sts)
st
{4, 5}
st = {1,2,3,4,5}
st.difference(sts)
{1, 2, 3}
st.symmetric
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    st.symmetric
AttributeError: 'set' object has no attribute 'symmetric'
_
st.symmetric_difference(sts)
{1, 2, 3, 6, 7, 8}
st.issuperset(sts)
False
st.issubset(sts)
False
st.isdisjoint(sts)
False
t= {1,2}
w = {5,6}
t.isdisjoint(w)
True
t.add("amit")
t
{1, 2, 'amit'}
t.remove(1)
t
{2, 'amit'}
w.clear()
w
set()
t.discard(2)
t
{'amit'}
t = {1, 2, 'amit'}
t.remove(3)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    t.remove(3)
KeyError: 3
t.discard(3)
t.pop()
'amit'
st = frozenset(st)
st
frozenset({1, 2, 3, 4, 5})
st.add(5)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    st.add(5)
AttributeError: 'frozenset' object has no attribute 'add'
st = set(st)
st
{1, 2, 3, 4, 5}
st.add(6)
st
{1, 2, 3, 4, 5, 6}
