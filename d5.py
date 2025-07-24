#strigs
s=('pavannagreddy')
s+('ravi')
s=s+('ravi')
k='pavan'
k
'pavan'
k+'ravi'
'pavanravi'
k
'pavan'
k=k+'ravi'
k
'pavanravi'
k
'pavanravi'
n='pavan'
n*5
'pavanpavanpavanpavanpavan'
'*'*6
'******'
'******'
'******'
#
name='pavan is good'
name.upper()
name='pavan is bad'
name.lower()
'pavan is bad'
name='anaju' nin here'
SyntaxError: unterminated string literal (detected at line 1)
name='kavya is cute'
name.capitalize()
'Kavya is cute'
name.swapcase()
'KAVYA IS CUTE'
name.title()
'Kavya Is Cute'
name.casefold()
'kavya is cute'
name='bbjh'
name.swapcase()
'BBJH'
name='bbjh'
name.casefold()
'bbjh'
name='pavan is good'
name.center(30,'*')
'********pavan is good*********'
name='kavya is inteligent'
name.center(30,'#')
'#####kavya is inteligent######'
name.ljust(40,'6')
           
'kavya is inteligent666666666666666666666'
\
name.rjust(60,'%')
           
'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%kavya is inteligent'
name.rjust(10,' ')
           
'kavya is inteligent'
name.rjust(40,' ')
           
'                     kavya is inteligent'
'22'.zfill(6)
           
'000022'
'54'.zfill(5)
           
'00054'
name
           
'kavya is inteligent'
name.find('kavya')
           
0
name.find('pavan')
           
-1
name.find('is')
           
6
name.rfind('v')
           
2
name.find('v')
           
2
name.rfind('t')
           
18
name.count('e')
           
2
'PFS30'.startswith('PFS')
           
True
for i in l:
    if i.startswith('pfs'):
           print(i)

           
pfs20
pfs30

for i in l:
    if i.endswith('png'):
        print(i)

           
demo.png
for i in l:
    if i.endswith('png'):
        print(i)

           
demo.png
for i in l:
    if i.endswith('pdf'):
        print(i)

           
resume.pdf
'abc'.isalpha
           
<built-in method isalpha of str object at 0x00000233AF337E10>
'abc'.isalpha()
           
True
'abc1'.isalpha()
           
False
'143'.isdigit()
           
True
'kavya22'.isalnum
           
<built-in method isalnum of str object at 0x00000233B1C3AF40>
'kavya22'.isalnum()
           
True
'pavan'.islower()
           
True
'Kavya'.islower()
           
False
'PAVAN'.isupper()
           
True
''.isspace()
           
False
' '.isspace()
           
True
'Hello Kavya'.istitle
           
<built-in method istitle of str object at 0x00000233B1C4C8B0>
'Hello Kavya'.istitle()
           
True
'1.2'.isdecimal()
           
False
'2223'.isdecimal()
           
True

'22'.isnumeric()
           
True
'character'.isidentifier()
           
True
'a'.isnumeric()
           
False
'pavan is here'
           
'pavan is here'

name='pavan is here'
           
name.replace('pavan','nag')
           
'nag is here'
name
           
'pavan is here'
name.split(' ')
           
['pavan', 'is', 'here']
name.split(*)
           
SyntaxError: Invalid star expression
name.split('*')
           
['pavan is here']
name.split('a')
           
['p', 'v', 'n is here']
name.rsplit()
           
['pavan', 'is', 'here']
#built in string functions
name=('pavan')
len(name)
5
max(name)
'v'
min(name)
'a'
name=('Pavan')
min(name)
'P'

ord('P')
80
ord('a')
    
97
sorted(name)
    
['P', 'a', 'a', 'n', 'v']
\
chr(80)
    
'P'
chr(86)
    
'V'
ord('v')
    
118
ord('V')
    
86
#splitting and joining mrthods
s='''Hello
welcome
everyone'''\


 
s
    
'Hello\nwelcome\neveryone'

s.splitlines()
    
['Hello', 'welcome', 'everyone']
['Hello', 'welcome', 'everyone']
    
['Hello', 'welcome', 'everyone']
s=['Hello', 'welcome', 'everyone']
''.join(s)
    
'Hellowelcomeeveryone'
' '.join(s)
    
'Hello welcome everyone'
'*'.join(s)
    
'Hello*welcome*everyone'
s='Hello*welcome*everyone'
    
s.partition(',')
    
('Hello*welcome*everyone', '', '')
s.rpartition(',')
    
('', '', 'Hello*welcome*everyone')

#whitespace and trimming methods
    
s='      pavan     '
    
s.strip()
    
'pavan'
s.rstrip()
    
'      pavan'
s.lstrip()
    
'pavan     '
#encodindg and decoding
    
s='Hello'
    
s.encode()
    
b'Hello'
text="Hello नमते你好 café 🙂"
    
text.encode()
    
b'Hello \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd caf\xc3\xa9 \xf0\x9f\x99\x82'

