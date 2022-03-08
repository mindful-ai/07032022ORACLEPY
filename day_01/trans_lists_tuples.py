Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ["red", "green", "blue", 1, 4.5, -65, [1,2,3]]
>>> type(L)
<class 'list'>
>>> # ------------------------ subscripting
>>> L[0]
'red'
>>> L[-1]
[1, 2, 3]
>>> L[1:4]
['green', 'blue', 1]
>>> L[::-1]
[[1, 2, 3], -65, 4.5, 1, 'blue', 'green', 'red']
>>> 
>>> # ----------------------- operators
>>> 
>>> [1,2,3] + [4,5,6]
[1, 2, 3, 4, 5, 6]
>>> [1,2,3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> len(L)
7
>>> type(L) == list
True
>>> isinstance(L, list)
True
>>> 'red' in L
True
>>> del L
>>> 
>>> # ------------------------- mutability
>>> 
>>> L = ["red", "green", "blue"]
>>> L[1]
'green'
>>> L[1] = "yellow"
>>> L
['red', 'yellow', 'blue']
>>> 
>>> L = ["red", "green", "blue"]
>>> L[1]
'green'
>>> L[1][1]
'r'
>>> L[1][1] = "R"
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    L[1][1] = "R"
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> L = ["red", "green", "blue", 1, 4.5, -65, [1,2,3]]
>>> L[-1][1] = '5'
>>> L
['red', 'green', 'blue', 1, 4.5, -65, [1, '5', 3]]
>>> 
>>> # ------------------------- add elements
>>> 
>>> L = ["red", "green", "blue"]
>>> L.append("yellow")
>>> L
['red', 'green', 'blue', 'yellow']
>>> L.insert(1, "orange")
>>> L
['red', 'orange', 'green', 'blue', 'yellow']
>>> L1 = ["black", "white"]
>>> L.extend(L1)
>>> L
['red', 'orange', 'green', 'blue', 'yellow', 'black', 'white']
>>> 
>>> # variations
>>> 
>>> L1
['black', 'white']
>>> L[1]
'orange'
>>> L[1] = L1
>>> L
['red', ['black', 'white'], 'green', 'blue', 'yellow', 'black', 'white']
>>> 
>>> L[2]
'green'
>>> L[2:3]
['green']
>>> L[2:3] = L1
>>> L
['red', ['black', 'white'], 'black', 'white', 'blue', 'yellow', 'black', 'white']
>>> # -------------------- remove elements
>>> 
>>> L
['red', ['black', 'white'], 'black', 'white', 'blue', 'yellow', 'black', 'white']
>>> L.pop()
'white'
>>> L.pop(1)
['black', 'white']
>>> L
['red', 'black', 'white', 'blue', 'yellow', 'black']
>>> L.remove("yellow")
>>> L
['red', 'black', 'white', 'blue', 'black']
>>> 
>>> 
>>> # ------------------ rearrange elements in a list
>>> 
>>> sorted(L)
['black', 'black', 'blue', 'red', 'white']
>>> L
['red', 'black', 'white', 'blue', 'black']
>>> reversed(L)
<list_reverseiterator object at 0x00000272D917D160>
>>> list(reversed(L))
['black', 'blue', 'white', 'black', 'red']
>>> L
['red', 'black', 'white', 'blue', 'black']
>>> 
>>> 
>>> L.sort()
>>> L
['black', 'black', 'blue', 'red', 'white']
>>> L.reverse()
>>> L
['white', 'red', 'blue', 'black', 'black']
>>> L.sort(reverse=True)
>>> L
['white', 'red', 'blue', 'black', 'black']
>>> 
>>> 
>>> # ----------------- search for elements
>>> 
>>> L
['white', 'red', 'blue', 'black', 'black']
>>> 'blue' in L
True
>>> L.count('blue')
1
>>> L.index('blue')
2
>>> 
>>> # -------------------- iterations
>>> 
>>> for item in L:
	print(item, end=' ')

	
white red blue black black 
>>> for item in L:
	print(item, ' --> ', len(item))

	
white  -->  5
red  -->  3
blue  -->  4
black  -->  5
black  -->  5
>>> 
>>> 
>>> # ---------------- numeric arrays
>>> 
>>> N = [1, 2, 3, 4, 4]
>>> sum(N)
14
>>> B = [True, True, False, True]
>>> any(B)
True
>>> all(B)
False
>>> 
>>> 
>>> # ------------ generation of values
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(20, 30))
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
>>> list(range(20, 50, 5))
[20, 25, 30, 35, 40, 45]
>>> list(range(10, 0, -1))
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> 
>>> # ----------------------- TUPLEs
>>> 
>>> T = ("red", "green", "blue")
>>> T[2]
'blue'
>>> T[2] = "yellow"
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    T[2] = "yellow"
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> sorted(T)
['blue', 'green', 'red']
>>> reversed(T)
<reversed object at 0x00000272D91C3860>
>>> 
>>> for item in T:
	print(item)

	
red
green
blue
>>> 
>>> N = (1, 2, 3)
>>> sum(N)
6
>>> B = (1, 2, 3, 0, -1, -2, -3)
>>> any(B)
True
>>> all(B)
False
>>> 
>>> # --- chainging the tuple: procedure
>>> T
('red', 'green', 'blue')
>>> L = list(T)
>>> L
['red', 'green', 'blue']
>>> L[0] = "RED"
>>> T = tuple(L)
>>> T
('RED', 'green', 'blue')
>>> 
>>> 
>>> # -------------- unpacking a tuple
>>> 
>>> r, g, b = T
>>> r
'RED'
>>> g
'green'
>>> b
'blue'
>>> 
>>> T = ('red', 'green', 'blue', 'yellow')
>>> r, g, b = T
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    r, g, b = T
ValueError: too many values to unpack (expected 3)
>>> r, g, *x = T
>>> r
'red'
>>> g
'green'
>>> x
['blue', 'yellow']
>>> 
