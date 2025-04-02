Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
st = "apple"
type(st)
<class 'str'>
st = "This is My Python Class"
st.lower()
'this is my python class'
st
'This is My Python Class'
st = st.lower()
st
'this is my python class'
st[0]
't'
st[0]="h"
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    st[0]="h"
TypeError: 'str' object does not support item assignment
st = "This is My Python Class"
st.upper()
'THIS IS MY PYTHON CLASS'
st.title()
'This Is My Python Class'
st.capitalize()
'This is my python class'
st.swapcase()
'tHIS IS mY pYTHON cLASS'
st.startswith("this")
False
st.startswith("This")
True
st.endswith("ss")
True
st.endswith("ass")
True
st.endswith("Ass")
False
st.islower()
False
st.isupper()
False
st.istitle()
False
st = "   This is My Python Class    "
st.strip()
'This is My Python Class'
st.lstrip()
'This is My Python Class    '
st.rstrip()
'   This is My Python Class'
st.index('s')
6
st = "This is My Python Class"
st.index(s)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    st.index(s)
NameError: name 's' is not defined
st = "This is My Python Class"
st.index('s')
3
st.rindex('s')
22
st.index('z')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    st.index('z')
ValueError: substring not found
>>> st.find('z')
-1
>>> st.find('s')
3
>>> st.count('s')
4
>>> st.count('s',6)
3
>>> st.count('s',22)
1
>>> st.count("s",1,22)
3
>>> st.partition("is")
('Th', 'is', ' is My Python Class')
>>> st.isdigit()
False
>>> sts = '12345'
>>> st.isdigit()
False
>>> sts.isdigit()
True
sts.isalpha()
False
st.isalpha()
False
st.isalnum()
False
sts.isnumeric()
True
st.split()
['This', 'is', 'My', 'Python', 'Class']
sts = st.split()
for i in st:
    print(i)

T
h
i
s
 
i
s
 
M
y
 
P
y
t
h
o
n
 
C
l
a
s
s
for i in sts:
    print(i)

This
is
My
Python
Class
st = "This,is, my, python"
st.split(",")
['This', 'is', ' my', ' python']
st.split("")
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    st.split("")
ValueError: empty separator
st = "thisismypython"
st.split('s')
['thi', 'i', 'mypython']
sts
['This', 'is', 'My', 'Python', 'Class']
" ".join(sts)
'This is My Python Class'
st.replace('s','q')
'thiqiqmypython'
st.replace('s','q',1)
'thiqismypython'
st = "Hello world"
st[3:8]
'lo wo'
st[::2]
'Hlowrd'
st[0:len(st):2]
'Hlowrd'
st[-3]
'r'
st[::-1]
'dlrow olleH'
st[len(st)-1:0:-1]
'dlrow olle'
st[len(st)-1:-1:-1]
''
st[len(st)-1:-12:-1]
'dlrow olleH'
st[len(st)-1:1:-1]
'dlrow oll'
