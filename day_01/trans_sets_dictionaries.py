Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # ------------------ SETS
>>> 
>>> s = "mississippi"
>>> list(s)
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> tuple(s)
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> set(s)
{'m', 'p', 'i', 's'}
>>> 
>>> s1 = set("abcdefgh")
>>> s1
{'h', 'g', 'f', 'e', 'd', 'a', 'b', 'c'}
>>> s2 = {'f', 'g', 'h', 'i', 'j', 'k', 'l'}
>>> s2
{'h', 'k', 'g', 'f', 'j', 'i', 'l'}
>>> 
>>> # ------------------- operations on sets
>>> 
>>> s1 & s2
{'g', 'h', 'f'}
>>> s1 | s2
{'h', 'k', 'g', 'f', 'j', 'e', 'i', 'd', 'a', 'l', 'b', 'c'}
>>> s1 ^ s2
{'k', 'j', 'e', 'i', 'd', 'a', 'l', 'b', 'c'}
>>> 
>>> 'a' in s1
True
>>> len(s1)
8
>>> s1 + s2
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s1 + s2
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> 
>>> 
>>> s1.add('x')
>>> s1
{'h', 'g', 'x', 'f', 'e', 'd', 'a', 'b', 'c'}
>>> s1.update({'y', 'z'})
>>> s1
{'h', 'z', 'g', 'x', 'f', 'e', 'd', 'a', 'y', 'b', 'c'}
>>> s1.remove('x')
>>> s1.union(s2)
{'h', 'k', 'z', 'g', 'f', 'j', 'e', 'i', 'd', 'a', 'l', 'b', 'y', 'c'}
>>> s1.intersection(s2)
{'g', 'h', 'f'}
>>> 
>>> 
>>> # ----------------------------------------------------------------
>>> 
>>> 
>>> 
>>> 
>>> # ------------------ DICTIONARIES
>>> 
>>> D = {'name':'Anil', 'age':35, 'company':'Oracle'}
>>> type(D)
<class 'dict'>
>>> type(s)
<class 'str'>
>>> type(S)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    type(S)
NameError: name 'S' is not defined
>>> type(s1)
<class 'set'>
>>> set
<class 'set'>
>>> 
>>> 
>>> D['name']
'Anil'
>>> D['age']
35
>>> D['company']
'Oracle'
>>> D['country']
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    D['country']
KeyError: 'country'
>>> D['country'] = 'India'
>>> D
{'name': 'Anil', 'age': 35, 'company': 'Oracle', 'country': 'India'}
>>> D.pop('age')
35
>>> D
{'name': 'Anil', 'company': 'Oracle', 'country': 'India'}
>>> 
>>> 
>>> D.keys()
dict_keys(['name', 'company', 'country'])
>>> D.values()
dict_values(['Anil', 'Oracle', 'India'])
>>> D.items()
dict_items([('name', 'Anil'), ('company', 'Oracle'), ('country', 'India')])
>>> 
