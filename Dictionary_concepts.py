Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dic = {}
dic["name"] = "Amit"
dic
{'name': 'Amit'}
dic = {"Name":"Amit","Class":5,"Roll no":6,"Marks":81}
dic
{'Name': 'Amit', 'Class': 5, 'Roll no': 6, 'Marks': 81}
dic['class']
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    dic['class']
KeyError: 'class'
dic["Class"]
5
dic.get('Marks')
81
dic.keys()
dict_keys(['Name', 'Class', 'Roll no', 'Marks'])
dic.values()
dict_values(['Amit', 5, 6, 81])
dic.items()
dict_items([('Name', 'Amit'), ('Class', 5), ('Roll no', 6), ('Marks', 81)])
dic.pop()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    dic.pop()
TypeError: pop expected at least 1 argument, got 0
dic.pop('Class')
5
dic
{'Name': 'Amit', 'Roll no': 6, 'Marks': 81}
dic.popitem()
('Marks', 81)
dic1
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    dic1
NameError: name 'dic1' is not defined. Did you mean: 'dic'?
dic1 = {"Class":8,"Marks":85}
dic.update(dic1)
dic
{'Name': 'Amit', 'Roll no': 6, 'Class': 8, 'Marks': 85}
dic1.clear()
dic1
{}
dic1 = dic.copy()
dic1
{'Name': 'Amit', 'Roll no': 6, 'Class': 8, 'Marks': 85}
class_5 = [{"Name":"Riya","Marks":65},{"Name":"siya","Marks":75},{"Name":"soni","Marks":85},{"Name":"Rahul","Marks":65}]
type(class_5)
<class 'list'>
class_5[1]
{'Name': 'siya', 'Marks': 75}
class_5[1]["Marks"]
75
>>> n = input("Enter your string")
Enter your string5 6 4
>>> type(n)
<class 'str'>
>>> dic = {'0':"Zero",'1':"One",'2':"Two",'3':"Three",'4':"Four",'5':"Five",'6':"Six"}
>>> st = n.split()
>>> st
['5', '6', '4']
>>> s = []
>>> for i in st:
...     s.append(dic.get(i))
... 
>>> s
['Five', 'Six', 'Four']
>>> s = " ".join(s)
>>> s
'Five Six Four'
>>> KeyboardInterrupt
