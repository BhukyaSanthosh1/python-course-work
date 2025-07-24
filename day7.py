class Tuple:
     def len(t):
         c=0
         for i in t:
             c+=1
         return c    
     def min(t)
     def max(t)
     def sum(t)
     def count(t)




class list:
     def append()
     def pop()
     def clear()
     def insert()
     def sort()
     def copy()
     def extend()
     def remove()
     def reverse()


#tuples

t=()
t=tuple()
t=(1,2,3,4,"string")
t
(1, 2, 3, 4, 'string')
t[4]
'string'

t[-5]
1
t[2]
3
t2=('python','list','tuple')
t=t2
t
('python', 'list', 'tuple')
t=(1,2,3,4,"string")
t2=('python','list','tuple')
t+t2
(1, 2, 3, 4, 'string', 'python', 'list', 'tuple')
t*3
(1, 2, 3, 4, 'string', 1, 2, 3, 4, 'string', 1, 2, 3, 4, 'string')
t+t2 * 4
(1, 2, 3, 4, 'string', 'python', 'list', 'tuple', 'python', 'list', 'tuple', 'python', 'list', 'tuple', 'python', 'list', 'tuple')
(t+t2)*4
(1, 2, 3, 4, 'string', 'python', 'list', 'tuple', 1, 2, 3, 4, 'string', 'python', 'list', 'tuple', 1, 2, 3, 4, 'string', 'python', 'list', 'tuple', 1, 2, 3, 4, 'string', 'python', 'list', 'tuple')
4 in t
True
5 in t
False
"kavya" in t
False
t=(1,2,3)
a,b,c=t
a
1
c
3
b
2
t=('kavya','pavan')
a,b=t
a
'kavya'
b
'pavan'

name,gmail,pwd=res
name
'anji'
gmail
'anji@gmail'
pwd
'anji@6122'
t=(1,1,1,2,2,3,4,4,5,5,5,5,5,6,9,9)

t.count(9)
2
t.count(5)
5
t.index(1)
0
len(t)
16
max(t)
9
min(t)
1
sum(t)
67
l=[1,2,3,4]
tuple(l)
(1, 2, 3, 4)

t[5].append(3)
t
(1, 2, 3, 4, 5, [1, 2, 3])
d=[('name','arun'),('gmial','arun@gmail.com'),('pwd','arun@122')]
dict(d)
{'name': 'arun', 'gmial': 'arun@gmail.com', 'pwd': 'arun@122'}

d={'name':'Tarak','mail':'Tarak@gmail.com','batch':'30','phoneno':'647485378'}
   
d['phoneno']
   
'647485378'
d['mail']
   
'Tarak@gmail.com'

d['batch']
   
'30'
d.get('age')
   

d
   
{'name': 'Tarak', 'mail': 'Tarak@gmail.com', 'batch': '30', 'phoneno': '647485378'}
d.get('age','Age is not there')
   
'Age is not there'
d={'name':'Tarak','mail;
d={'name':'Tarak','mail':'Tarak@gmail.com','batch':'30','phoneno':'647485378'}
   
SyntaxError: unterminated string literal (detected at line 1)
d={'name':'Tarak','mail':'Tarak@gmail.com','batch':'30','phoneno':'647485378'}
   
d={'name':'Tarak','mail':'Tarak@gmail.com','batch':'30','phoneno':'647485378'}

d={'name':'Tarak','mail':'Tarak@gmail.com','batch':'30','phoneno':'647485378'}
   
d['name']='tommy'
   
d
   
{'name': 'tommy', 'mail': 'Tarak@gmail.com', 'batch': '30', 'phoneno': '647485378'}
d.pop('mail')
   
'Tarak@gmail.com'
d
   
{'name': 'tommy', 'batch': '30', 'phoneno': '647485378'}

del d['phoneno']
   
d
   
{'name': 'tommy', 'batch': '30'}

d.clear()
   
d
   
{}
d=['name': 'tommy', 'mail': 'Tarak@gmail.com', 'batch': '30', 'phoneno': '647485378']
   
SyntaxError: invalid syntax
d={'name':'Tarak','mail':'Tarak@gmail.com','batch':'30','phoneno':'647485378'}
   
d.get('name','name is not del')
   
'Tarak'
d.keys()
   
dict_keys(['name', 'mail', 'batch', 'phoneno'])

d.values()
   
dict_values(['Tarak', 'Tarak@gmail.com', '30', '647485378'])
d.items()
   
dict_items([('name', 'Tarak'), ('mail', 'Tarak@gmail.com'), ('batch', '30'), ('phoneno', '647485378')])
d
   
{'name': 'Tarak', 'mail': 'Tarak@gmail.com', 'batch': '30', 'phoneno': '647485378'}
d.update({'key1':123,'key2':456
          d
          
SyntaxError: '{' was never closed
        d.update({'key1':123,'key2':456})
          
SyntaxError: unexpected indent
d.update({'key1':123,'key2':456})
          
d
          
{'name': 'Tarak', 'mail': 'Tarak@gmail.com', 'batch': '30', 'phoneno': '647485378', 'key1': 123, 'key2': 456}
del d['key2']
          
d
          
{'name': 'Tarak', 'mail': 'Tarak@gmail.com', 'batch': '30', 'phoneno': '647485378', 'key1': 123}
d.setdefault('batch','pfs')
          
'30'
d
          
{'name': 'Tarak', 'mail': 'Tarak@gmail.com', 'batch': '30', 'phoneno': '647485378', 'key1': 123}
d.setdefault('course','pfs')
          
'pfs'
d
          
{'name': 'Tarak', 'mail': 'Tarak@gmail.com', 'batch': '30', 'phoneno': '647485378', 'key1': 123, 'course': 'pfs'}
len(d)
          
6
max(d)
          
'phoneno'
min(d)
          
'batch'

['batch', 'course', 'key1', 'mail', 'name', 'phoneno']
d['SKILLSRATING']={'python':4,'java':3,'c++':2}
          
d
          
{'name': 'Tarak', 'mail': 'Tarak@gmail.com', 'batch': '30', 'phoneno': '647485378', 'key1': 123, 'course': 'pfs', 'SKILLSRATING': {'python': 4, 'java': 3, 'c++': 2}}
