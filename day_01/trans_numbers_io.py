Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # --------------------- NUmbers
>>> 
>>> 
>>> # Arithmetic Operators
>>> # +, -, *, /, % , //, **
>>> 
>>> a = 10
>>> b = 3
>>> a / b
3.3333333333333335
>>> a % b
1
>>> a // b
3
>>> a ** b
1000
>>> 
>>> # Relational operators
>>> # ==, !=, >=, <=, <, >
>>> 
>>> a > b # Is a greater than b?
True
>>> a == b*3+1
True
>>> a == b
False
>>> 
>>> # Logical Operators
>>> # and, or, not
>>> 
>>> a > b and a < 10
False
>>> a > b and not a < 10
True
>>> a > b or a < 10
True
>>> 
>>> # in-built functions
>>> 
>>> a = 100
>>> type(a)
<class 'int'>
>>> type(a) == int
True
>>> isinstance(a, str)
False
>>> 
>>> 
>>> bin(a)
'0b1100100'
>>> oct(a)
'0o144'
>>> hex(a)
'0x64'
>>> s = '100'
>>> s + 10
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s + 10
TypeError: can only concatenate str (not "int") to str
>>> int(s) + 10
110
>>> 
>>> s = '10110101'
>>> int(s)
10110101
>>> int(s, 2)
181
>>> bin(181)
'0b10110101'
>>> 
>>> 
>>> # ------------------ built-in modules
>>> 
>>> a = 90
>>> sin(a)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    sin(a)
NameError: name 'sin' is not defined
>>> import math
>>> math.sin(90)
0.8939966636005579
>>> math.sin(90 * 3.14/180)
0.9999996829318346
>>> math.sin(90 * math.pi / 180)
1.0
>>> math.sin(math.radians(a))
1.0
>>> 

>>> # ------------------------------------- user io
>>> 
>>> print("The number is : ", a)
The number is :  90
>>> 
>>> 
>>> input()
12
'12'
>>> a = input()
45
>>> a
'45'
>>> a = input("Enter a number : ")
Enter a number : 56
>>> a
'56'
>>> math.sqrt(a)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    math.sqrt(a)
TypeError: must be real number, not str
>>> math.sqrt(int(a))
7.483314773547883
>>> 
>>> b = int(input("Enter a number: "))
Enter a number: 67
>>> math.sqrt(b)
8.18535277187245
>>> 
