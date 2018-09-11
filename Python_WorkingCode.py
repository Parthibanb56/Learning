Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print ("hai")
hai
>>> 
KeyboardInterrupt
>>> print "Start"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Start")?
>>> print ("start")
start
>>> A="Variable Test"
>>> print A
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(A)?
>>> print(A)
Variable Test
>>> print (A+" "+"Concat")
Variable Test Concat
>>> varflot=10.5
>>> varint=10
>>> print (varflot+varint)
20.5
>>> x=y=z=50
>>> print (iple)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print (iple)
NameError: name 'iple' is not defined
>>> tuple=(1,2,3,"four")
>>> print tuple[2]
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(tuple[2])?
>>> print (tuple[2])
3
>>> print tuple[2:]
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(tuple[2:])?
>>> print (tuple[:2])
(1, 2)
>>> print (tuple[1:])
(2, 3, 'four')
>>> print (tuple[2:1])
()
>>> print (tuple[:3])
(1, 2, 3)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> dict={'var1':1,'var2':2,'var3':3}
>>> dict.keys()
dict_keys(['var1', 'var2', 'var3'])
>>> dict['var1']
1
>>> dict.values()
dict_values([1, 2, 3])
>>> dict={'var1':1,'var2':2,'var3':3,'var4':"test"}
>>> dict.values
<built-in method values of dict object at 0x02DB6480>
>>> dict.values()
dict_values([1, 2, 3, 'test'])
>>> dict[var1]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    dict[var1]
NameError: name 'var1' is not defined
>>> dict['var2']
2
>>> # Variables
>>> a,b,c=10,20,30
>>> print (a)
10
>>> print (a+b+c)
60
>>> c=10.4
>>> print (b+c)
30.4
>>> # Tuple
>>> tup=(10,"tup1",20,"tup2")
>>> print (tup[1])
tup1
>>> print (tup[:2])
(10, 'tup1')
>>> # Dictionary
>>> dict={10,"dic1",20,"dic2"}
>>> dict={'v1':10,'v2':"dic1",'v3':20,'v4':"dic2"}
>>> dict.keys()
dict_keys(['v1', 'v2', 'v3', 'v4'])
>>> dict.values()
dict_values([10, 'dic1', 20, 'dic2'])
>>> dict[2]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    dict[2]
KeyError: 2
>>> dict['v2']
'dic1'
>>> dict[v2]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    dict[v2]
NameError: name 'v2' is not defined
>>> dict['v5']
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    dict['v5']
KeyError: 'v5'
>>> # Identifier
>>> _name="Python"
>>> print (_name)
Python
>>> print (_Name)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    print (_Name)
NameError: name '_Name' is not defined
>>> # Python Literals

>>> a="test\
test1"
>>> print (a)
testtest1
>>> print ('''test
test1
test2
test3''')
test
test1
test2
test3
>>> # list
>>> list1=[1,2,"three"]
>>> list1[2]
'three'
>>> list1[1:1]
[]
>>> list1[1:1]
[]
>>> list1[1:]
[2, 'three']
>>> list1[1:2]
[2]
>>> list1*2
[1, 2, 'three', 1, 2, 'three']
>>> list2=list1*2
>>> print (list1)
[1, 2, 'three']
>>> print (list2)
[1, 2, 'three', 1, 2, 'three']
>>> list2[1:2]
[2]
>>> list2[2:3]
['three']
>>> list2[2:4]
['three', 1]
>>> 
