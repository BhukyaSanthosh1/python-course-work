1.string input
   
name=input("enter the name")
   
enter the name python
name
   
' python'
type(name)
   
<class 'str'>
age=input("enter the age:")
   
enter the age:60
age
   
'60'
type(age)
   
<class 'str'>
age=int(input("enter the age:"))
   
enter the age:22
type(age)
   
<class 'int'>
discount=float(input("enter the discount:"))
   
enter the discount:23
discount
   
23.0
type(discount)
   
<class 'float'>
grade=float(input("75"))
   
75
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    grade=float(input("75"))
ValueError: could not convert string to float: ''
grade=float(input("75"))
   
75 type(grade)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    grade=float(input("75"))
ValueError: could not convert string to float: ' type(grade)'
names=input("enter the names:")
   
enter the names:rajeswari kusuma kavya
names
   
'rajeswari kusuma kavya'
names=input("enter the names:").split()
   
enter the names:rajeswari kusuma kavya
\
names
   
['rajeswari', 'kusuma', 'kavya']
num=input("enter numbers:").split
   
enter numbers:1 4 3 3


num=map(int,input("enter numbers:").split())
   
enter numbers:1 2 3 4 5
num
   
<map object at 0x0000019A42B2BB80>
num=list(map(int,input("enter numbers:").split()))
   
enter numbers:1 2 3 4 5
num
   
[1, 2, 3, 4, 5]
num=list(map(float,input("enter numbers:").split()))
   
enter numbers:1 2 3 4 5
num
   
[1.0, 2.0, 3.0, 4.0, 5.0]
num=list(map(str,input("enter numbers:").split()))
   
enter numbers:oeri hhjh jfug kkheg 
num
   
['oeri', 'hhjh', 'jfug', 'kkheg']
num=tuple(map(str,input("enter numbers:").split()))
   
enter numbers:1 2 3 4 5
num
   
('1', '2', '3', '4', '5')
num=tuple(map(float,input("enter numbers:").split()))
   
enter numbers:4 5 7 8 
num
   
(4.0, 5.0, 7.0, 8.0)
num=set(map(float,input("enter numbers:").split()))
   
enter numbers:3 4 5 6
num
   
{3.0, 4.0, 5.0, 6.0}
num=set(input("enter numbers:").split())
   
enter numbers:7 5 4 3
num
   
{'3', '5', '4', '7'}
num
   
<built-in method split of str object at 0x0000019A42B2A8E0>
num=input("enter numbers:").split
   
enter numbers:1 2 3 4
num
   
<built-in method split of str object at 0x0000019A42B2B870>
num=input("enter numbers:").split()
   
enter numbers:1 2 3 4
num
   
['1', '2', '3', '4']

num=eval(input("enter dict:"))
     
enter dict:{'name':'pavan','age':21}
num
     
{'name': 'pavan', 'age': 21}
n=bool(input("enter the status:"))
     
enter the status:false
n
     
True
name,email,pwd=input("enter the data:").split()
     
enter the data:anji anji@gmail.com anji@122
name
     
'anji'
pwd
     
'anji@122'
email
     
'anji@gmail.com'




#output formatting
     
a,b,c=12,23.4,'string'
     
a
     
12
c
     
'string'
b
     
23.4
print(a,b,c)
     
12 23.4 string
print("a:",a,'b:',b,'c:',c)
     
a: 12 b: 23.4 c: string
print('%d,%f,%s'%(a,b,c))
     
12,23.400000,string
#modulo operator
     
#last one
     
print('a: %d b: %f c: %s'%(a,b,c))
     
a: 12 b: 23.400000 c: string
print(f'{a} {b} {c}')
     
12 23.4 string
print(f'a:{a}\nb:{b}\nc:{c}')
     
a:12
b:23.4
c:string
print('a: {2}\nb: {0}\nc: {1}'.format(a,b,c))
     
a: string
b: 12
c: 23.4
print(a,b,c)
     
12 23.4 string
print(a,b,c,sep='@')
     
12@23.4@string
print(a,b,c,sep='@',end='\\\\\\\\\\'))
            
SyntaxError: unmatched ')'
print(a,b,c,sep='@',end='\\\\\\\\\\')
            
12@23.4@string\\\\\\
print(a)
            
12

