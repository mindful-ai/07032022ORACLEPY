Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Strings
>>> 
>>> 
>>> s = "computer"
>>> type(s)
<class 'str'>
>>> 
>>> # ---------------- subscripting
>>> # [index]
>>> # [start:end]
>>> # [start:end:interval]
>>> 
>>> s[0]
'c'
>>> s[1]
'o'
>>> s[-1]
'r'
>>> s[-2]
'e'
>>> s[3:7]
'pute'
>>> s[0:5]
'compu'
>>> s[:5]
'compu'
>>> s[5:8]
'ter'
>>> s[5:]
'ter'
>>> s[:]
'computer'
>>> s[1:7]
'ompute'
>>> s[1:7:2]
'opt'
>>> s[::3]
'cpe'
>>> s[::-1]
'retupmoc'
>>> s[1:7]
'ompute'
>>> s[1:7:-1]
''
>>> s[1:7][::-1]
'etupmo'
>>> s[-5:-1]
'pute'
>>> # --------------------------- immutability
>>> 
>>> s
'computer'
>>> s[4]
'u'
>>> s[4] = "I"
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s[4] = "I"
TypeError: 'str' object does not support item assignment
>>> 
>>> # --------------------------- operators
>>> 
>>> s
'computer'
>>> s + 's'
'computers'
>>> s * 3
'computercomputercomputer'
>>> len(s)
8
>>> "put" in s
True
>>> type(s) == str
True
>>> isinstance(s, str)
True
>>> del s
>>> s
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> 
>>> # --------------------------- functions
>>> 
>>> 
>>> # --------- case
>>> 
>>> s = "computer"
>>> s.upper()
'COMPUTER'
>>> s.lower()
'computer'
>>> s.capitalize()
'Computer'
>>> 
>>> 
>>> # ------------ checking
>>> 
>>> '123'.isdigit()
True
>>> '123a'.isdigit()
False
>>> '123a'.isalpha()
False
>>> '123a'.isalnum()
True
>>> ' '.isspace()
True
>>> 'This Is Python Training Progam'.istitle()
True
>>> 
>>> # -------------- searching
>>> 
>>> 'p' in s
True
>>> s.find("ter")
5
>>> s.rfind("ter")
5
>>> s1 = "apples"
>>> s1.count('p')
2
>>> 
>>> # --------------- strings modificaiton
>>> 
>>> # stripping
>>> 
>>> s2 = '   12345  '
>>> s2.strip()
'12345'
>>> s2.lstrip()
'12345  '
>>> s2.rstrip()
'   12345'
>>> 
>>> 
>>> # justificaiton
>>> s
'computer'
>>> s.ljust(20)
'computer            '
>>> s.rjust(20, '>')
'>>>>>>>>>>>>computer'
>>> 
>>> 
>>> # replacing characters
>>> 
>>> ip = "127-0-0-1"
>>> ip.replace('-', '.')
'127.0.0.1'
>>> ip
'127-0-0-1'
>>> newip = ip.replace('-', '.')
>>> newip
'127.0.0.1'
>>> 
>>> # splitting and joining
>>> 
>>> text = "mary had a little lamb"
>>> words = text.split()
>>> words
['mary', 'had', 'a', 'little', 'lamb']
>>> text.split('a')
['m', 'ry h', 'd ', ' little l', 'mb']
>>> 
>>> 
>>> words
['mary', 'had', 'a', 'little', 'lamb']
>>> '-'.join(words)
'mary-had-a-little-lamb'
>>> 
>>> 
>>> # string formatting
>>> 
>>> "my name is {} and age is {}".format("Anil", 35)
'my name is Anil and age is 35'
>>> "my name is {0} and age is {1}".format("Anil", 35)
'my name is Anil and age is 35'
>>> "my name is {1} and age is {0}".format("Anil", 35)
'my name is 35 and age is Anil'
>>> "my name is {name} and age is {age}".format(name="Anil", age=35)
'my name is Anil and age is 35'
>>> "my name is {1:10} and age is {0:5}".format("Anil", 35)
'my name is         35 and age is Anil '
>>> "my name is {1:<10} and age is {0:>5}".format("Anil", 35)
'my name is 35         and age is  Anil'
>>> "my name is {1:^10} and age is {0:^5}".format("Anil", 35)
'my name is     35     and age is Anil '
>>> 
>>> template = "my name is {1:^10} and age is {0:^5}"
>>> template.format("Raj", 45)
'my name is     45     and age is  Raj '
>>> 
>>> 
>>> # translations

>>> s
'computer'
>>> tt = s.maketrans({'p':'P', 'u':'U', 't':'TT'})
>>> tt
{112: 'P', 117: 'U', 116: 'TT'}
>>> s.translate(tt)
'comPUTTer'
>>> s
'computer'
>>> 
