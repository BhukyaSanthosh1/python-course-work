#conditional statements
'''data={
'pavan@gmail.com':'1234@',
'anji@gmail.com':'3870@',
'prasad@gmail.com':'93004@,'
}
email,pwd=input("enter the email and pwd: ").split()
if data.get(email)==pwd:
    print('login succesful')
else:
    print('invalid login')'''


#2
'''items=['coffee','samosa','idly','ice cream']
data=input("enter the item")
if data in items:
    print("ava")
else:
    print("NA")'''

#3
'''items=['coffee','samosa','idly','ice cream','biryani']
stocks=[10,33,45,26,23]
data=input("enter the item:")
if data in items:
    ind=items.index(data)
    if stocks[ind]>0:
        print("ava")
    else:
        print('out of stock.please try again')
else:
    print('item not ava')'''
    
        
#4
'''items=['coffee','samosa','idly','ice cream']
stocks=[10,33,45,26,23]
distance=[13,4,9,12]
ratings=[3.2,4,4,1]
cost=[150,60,20,40]
veg=[True,True,False,True]
time=[40,30,25,15]
data=input("enter the item:")
ind=items.index(data)
if distance[ind]<5 and ratings[ind]>4 and cost[ind]<500 and veg[ind] and time[ind]<30:
    print('time,veg,cost,distance and ratings applied')
elif distance[ind]<5 and ratings[ind]>4 and cost[ind]<500 and veg[ind]:
    print('veg,cost,distance and ratings applied')
elif distance[ind]<5 and ratings[ind]>4 and cost[ind]<500:
    print('cost,distance and ratings applied')
elif  distance[ind]<5 and ratings[ind]>4:
    print('distance and ratings applied')
elif  ratings[ind]>4:
    print('ratings applied')
elif distance[ind]<5:
    print('distance applied')
elif cost[ind]<500:
    print('cost applied')
elif veg[ind]:
    print('veg applied')
elif time[ind]<30:
    print('time applied')
else:
    print('show all products')'''


#5
'''num=int(input("enter the number"))
if num&2==0 and num%3==0:
    print('divisible by  2 and 3')
elif num%2==0:
    print('True')
elif num%3==0:
    print('False')
else:
    print('not divisible')'''


#6
'''num=int(input("enter the number"))
if num&2==0:
    print('Even')
else:
    print('Odd')'''


#7
'''num=int(input("enter the number"))
if num%400==0 or(num%4==0 and num%100!=0):
    print("leap year")
else:
    print('not leap year')'''


#8
'''num=input("enter the number")
if num==num[::-1]:
    print('palindrone')
else:
    print('not palindrone')'''

#9
'''age=int(input("enter the age"))
if age>=18:
        print('eligible to vote')
else:
    print('not eligible')'''
    
#10
'''a=int(input("enter a:"))
b=int(input("enter b:"))
if a>b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")'''

#11
'''a=int(input("enter a:"))
b=int(input("enter b:"))
if a>b:
    print(f"{a} is greater than {b}")
elif a==b:
    print(f"{a} is equal to {b}")    
else:
    print(f"{b} is greater than {a}")'''

#12
'''a=int(input("enter a:"))
if a%2==0 and a%3==0:
    print(f"a is divisible")
elif a%2==0:
    print(f"only 2")
elif a%3==0:
    print (f"only 3")
else:
    print(f"not divisible")'''
        

