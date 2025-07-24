Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets
s=set()
s=[1,2,3,3,4,5,6]
s
[1, 2, 3, 3, 4, 5, 6]
s={1,2,3,"string",(1,2,3),3+8j}
class30=(arun,gopal,santhosh,pavan'
         
SyntaxError: unterminated string literal (detected at line 1)
class30=('arun','gopal','santhosh','pavan')
         
class30
         
('arun', 'gopal', 'santhosh', 'pavan')
'pavan' in class30
         
True
'shmitha' in class30
         
False
girls={'shmitha','rajeshwari','sravani'}
         
boys={'santhosh','rajeshwari','sravani'}
         
girls | boys
         
{'rajeshwari', 'sravani', 'shmitha', 'santhosh'}
girls & boys
         
{'rajeshwari', 'sravani'}
girls={'shmitha','rajeshwari','sravani'}
         
boys={'santhosh','pavan','rakesh'}
         
girls|boys
         
{'rajeshwari', 'pavan', 'rakesh', 'sravani', 'shmitha', 'santhosh'}
girls&boys
         
set()
girls-boys
         
{'shmitha', 'rajeshwari', 'sravani'}
girls={'shmitha','rajeshwari','sravani'}
         
boys={'santhosh','pavan','rajeshwari'}
         
girls<=boys
         
False
girls^boys
         
{'sravani', 'shmitha', 'santhosh', 'pavan'}
girls={'shmitha','rajeshwari','sravani'}boys={'santhosh','pavan','rajeshwari'}
         
SyntaxError: invalid syntax
girls={'shmitha','rajeshwari','sravani'}
         
boys={'santhosh','pavan','rajeshwari','shmitha','sravani'}
         
girls<=boys
         
True
boys={'santhosh','pavan','rajeshwari','shmitha','sravani'}
         
girls={'shmitha','rajeshwari','sravani'}
         
boys>=girls
         
True
boys={'santhosh','pavan','rajeshwari','shmitha','sravani'}
         
girls={'shmitha','rajeshwari','sravani'}
         
boys.isdisjoint(girls)
         
False
# 4.built-in methods for sets cheyali
girls={'shmitha','rajeshwari','sravani'}
girls.add('pavani')
girls
{'sravani', 'rajeshwari', 'shmitha', 'pavani'}
girls.remove('sravani')
girls
{'rajeshwari', 'shmitha', 'pavani'}
girls.discard([sravani')
               
SyntaxError: unterminated string literal (detected at line 1)

girls.discard('sravani')
               
girls
               
{'rajeshwari', 'shmitha', 'pavani'}
girls.pop()
               
'rajeshwari'
girls.pop()
               
'shmitha'
boys
girls
               
{'pavani'}
girls.clear()
               
girls
               
set()
girls={'shmitha','rajeshwari','sravani'}
               
girls.update({'pavani','naveena'})
               
girls
               
{'sravani', 'naveena', 'shmitha', 'pavani', 'rajeshwari'}
a={1,2,3,4}
               
b={3,4,5,6}
               
a  | b
               
{1, 2, 3, 4, 5, 6}
a & b
               
{3, 4}
a.intersection_update(b)
               
a
               
{3, 4}
b
               
{3, 4, 5, 6}
c=a.copy()
               
c.add(7)
               
c
               
{3, 4, 7}
a
               
{3, 4}
d=a
d.add(20)
               
d
               
{3, 4, 20}
girls
               
{'sravani', 'naveena', 'shmitha', 'pavani', 'rajeshwari'}
len(girls)
               
5
max(girls)
               
'sravani'
min(girls)
               
'naveena'
a
               
{3, 4, 20}
sum(a)
               
27
sorted(a)
               
[3, 4, 20]
sorted(girls)
               
['naveena', 'pavani', 'rajeshwari', 'shmitha', 'sravani']

                                
#5.built in functions for sets
         
girls
         
{'shmitha', 'rajeshwari', 'sravani'}
{'shmitha', 'rajeshwari', 'sravani','sandy','pandu'}
         
{'rajeshwari', 'pandu', 'sandy', 'sravani', 'shmitha'}
len(girls)
         
3
girls={'shmitha', 'rajeshwari', 'sravani','sandy','pandu'}
         
len(girls)
         
5
max(girls)
         
'sravani'
min(girls)
         
'pandu'
         a={1,2,3,4}
         
sum(a)
         
10
a={9,1,5,2,3,4}
         
sorted(a)
         
[1, 2, 3, 4, 5, 9]

s=[1,2,3]
               
set(s)
               
{1, 2, 3}
f=frozenset({1,2,3,4})
               
type(f)
               
<class 'frozenset'>
len(f)
               
4         
