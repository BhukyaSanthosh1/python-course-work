 ====================================================================
#type conversion(type casting)
a=12
float(a)
12.0
a='pavan'
str(a)
'pavan'
bool(a)
True
str(a)
'pavan'
a=12
str(a)
'12'
float(a)
12.0
bool(a)
True
list()
[]
list(s)
s=['p','y','t','h','o','n']
list(s)
['p', 'y', 't', 'h', 'o', 'n']
bool(s)
True
l=['1,2,3,4,']
str()
''
str(l)
"['1,2,3,4,']"
l
['1,2,3,4,']
s='python'
set(s)
{'t', 'p', 'o', 'h', 'y', 'n'}
tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
l=['1,2,3,4']
l
['1,2,3,4']
l=['1','2','3','4']
''.join(l)
'1234'
tuple(l)
('1', '2', '3', '4')
set(1)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(1)
TypeError: 'int' object is not iterable
set(l)
{'2', '1', '4', '3'}
bool(l)
True
t=(1,2,3)
int(t)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
list(t)
[1, 2, 3]
set(t)
{1, 2, 3}
dict(t)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
str(t)
'(1, 2, 3)'
bool(t)
True
t=[('coursre'.'py'),('batch'.'30')]
SyntaxError: invalid syntax
t=[('coursre'.'py'),('batch'.'30')]
SyntaxError: invalid syntax
t=[('coursre','py'),('batch','30')]
dict(t)
{'coursre': 'py', 'batch': '30'}
a={1,2,3,4}
int(a)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(a)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'set'
complex(a)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    complex(a)
TypeError: complex() first argument must be a string or a number, not 'set'
str(a)
'{1, 2, 3, 4}'
list(a)
[1, 2, 3, 4]
tuple(a)
(1, 2, 3, 4)
dict(a)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    dict(a)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(a)
True
d={'course':'py',''batch':30}
   
SyntaxError: unterminated string literal (detected at line 1)
d={'course':'py','batch':30}
   
int(d)
   
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
   
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(d)
   
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'dict'
list(d)
   
['course', 'batch']
tuple(d)
   
('course', 'batch')
set(d)
   
{'course', 'batch'}
bool(d)
   
True
