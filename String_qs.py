Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
st = "This is the python class"
st = st.split()
st
['This', 'is', 'the', 'python', 'class']
for i in st:
    if(len(i)%2 == 0):
        print(i)

This
is
python
st[::-1]
['class', 'python', 'the', 'is', 'This']
st
['This', 'is', 'the', 'python', 'class']
st = st[::-1]
st
['class', 'python', 'the', 'is', 'This']
" ".join(st)
'class python the is This'
st
['class', 'python', 'the', 'is', 'This']
st = " ".join(st)
st
'class python the is This'
st = "abbbcbbba"
rev = st[::-1]
rev
'abbbcbbba'
if rev == st:
    print("String is palindrome")
else:
    print("String is not palindrome")

String is palindrome
st = "abc"
rev = st[::-1]
if rev == st:
...     print("String is palindrome")
... else:
...     print("String is not palindrome")
... 
String is not palindrome
>>> st = "Brain,mentors.and,skill,risers."
>>> #Brain.mentors,and.skill.risers,
>>> st = st.replace(',','.')
>>> st = st.replace('.',',')
>>> st
'Brain,mentors,and,skill,risers,'
>>> m = st.replace(',','.')
>>> m
'Brain.mentors.and.skill.risers.'
>>> st = "Brain,mentors.and,skill,risers."
>>> st = st.replace(",","temp")
>>> st = st.replace(".",",")
>>> st = st.replace("temp",".")
>>> st
'Brain.mentors,and.skill.risers,'
