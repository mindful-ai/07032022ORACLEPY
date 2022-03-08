Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # ---------- LOOPS ------------------- #
>>> 
>>> 
>>> print('5', ' X ', '1', ' = ', (5*1))
5  X  1  =  5
>>> for i in range(1, 11):
	print('5', ' X ', i, ' = ', (5*i))

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> D = {'name':'Anil', 'age':35, 'company':'Oracle', 'country':'India'}
>>> for k, v in D.items():
	print(k.rjust(8), ' | ', v.ljust(8))

	
    name  |  Anil    
Traceback (most recent call last):
  File "<pyshell#11>", line 2, in <module>
    print(k.rjust(8), ' | ', v.ljust(8))
AttributeError: 'int' object has no attribute 'ljust'
>>> for k, v in D.items():
	print(k.rjust(8), ' | ', str(v).ljust(8))

	
    name  |  Anil    
     age  |  35      
 company  |  Oracle  
 country  |  India   
>>> 
>>> 
>>> # -------------------------- loop control statements
>>> 
>>> for i in range(1, 11):
	print('5', ' X ', i, ' = ', (5*i))
	if(i == 5):
		break;

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
>>> for i in range(1, 11):
	if(i % 3 == ):
		
SyntaxError: invalid syntax
>>> for i in range(1, 11):
	if(i % 3 == ):
		
SyntaxError: invalid syntax
>>> for i in range(1, 11):
	if(i % 3 == 0):
		continue
	print('5', ' X ', i, ' = ', (5*i))

	
5  X  1  =  5
5  X  2  =  10
5  X  4  =  20
5  X  5  =  25
5  X  7  =  35
5  X  8  =  40
5  X  10  =  50
>>> 
>>> 
>>> # ----------------- while
>>> 
>>> i = 1
>>> while i <= 10;
SyntaxError: invalid syntax
>>> while i <= 10:
	print('5', ' X ', i, ' = ', (5*i))
	i += 1

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
