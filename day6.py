#lists
    
l=[1,2,3,4,5]
    
l
    
[1, 2, 3, 4, 5]
l.append(7)
    
l
    
[1, 2, 3, 4, 5, 7]

l
[1, 2, 3, 4, 5, 7]
l.remove(2)





l
[1, 3, 4, 5, 7]
l
[1, 3, 4, 5, 7, '2.3', 'string', {'Pavan': 'pavan'}]
l[3:7]
[5, 7, '2.3', 'string']
l[-1:5]
[]
l
[1, 3, 4, 5, 7, '2.3', 'string', {'Pavan': 'pavan'}]
l[-1:-5]
[]
l[-1:-5:-1]
[{'Pavan': 'pavan'}, 'string', '2.3', 7]
#adding elements
l
[1, 3, 4, 5, 7, '2.3', 'string', {'Pavan': 'pavan'}]
l.append('kavya')
l
[1, 3, 4, 5, 7, '2.3', 'string', {'Pavan': 'pavan'}, 'kavya']
l.insert(5,5)
l
[1, 3, 4, 5, 7, 5, '2.3', 'string', {'Pavan': 'pavan'}, 'kavya']

l
         
[1, 3, 4, 5, 7, 5, '2.3', 'string', {'Pavan': 'pavan'}, 'kavya']
l.extend(['abhi',22])
         
l
         
[1, 3, 4, 5, 7, 5, '2.3', 'string', {'Pavan': 'pavan'}, 'kavya', 'abhi', 22]
l.remove(22)
         
l
         
[1, 3, 4, 5, 7, 5, '2.3', 'string', {'Pavan': 'pavan'}, 'kavya', 'abhi']


l.pop(7)
         
'string'
l
         
[1, 3, 4, 5, 7, 5, '2.3', {'Pavan': 'pavan'}, 'kavya', 'abhi']
l.count(5)
         
2
l.count('pavan')
         
0
l.count('kavya')
         
1
l=[122,4,67,3,4,67,32,24,95,23]
         
sorted(l)
         
[3, 4, 4, 23, 24, 32, 67, 67, 95, 122]
l.sort(reverse=True)
         
l
         
[122, 95, 67, 67, 32, 24, 23, 4, 4, 3]
l.reverse()
         
l
         
[3, 4, 4, 23, 24, 32, 67, 67, 95, 122]
k=l.copy()
         
k
         
[3, 4, 4, 23, 24, 32, 67, 67, 95, 122]
k.append(22)
         
k
         
[3, 4, 4, 23, 24, 32, 67, 67, 95, 122, 22]
m=l
         
m
         
[3, 4, 4, 23, 24, 32, 67, 67, 95, 122]
m.append(25)
         
m
         
[3, 4, 4, 23, 24, 32, 67, 67, 95, 122, 25]
max(m)
         
122
min(m)
         
3
sum(l)
         
466
len(m)
         
11
all(m)
         
True
m.append(0)
         
m
         
[3, 4, 4, 23, 24, 32, 67, 67, 95, 122, 25, 0]
all(m)
         
False
any(m)
         
True
m=[0,0,0,0,0]
         
any(m)
         
False
m.append(1)
         
m
         
[0, 0, 0, 0, 0, 1]
any(m)
         
True


