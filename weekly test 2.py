#1.automated salary tax calculator
'''salary=float(input())
if salary <= 25000:
    print("no tax")
elif salary >25000 and salary <=50000:
    print(salary*0.05)
elif salary >50000 and salary<=100000:
    print(salary*0.2)
else:
    print(salary*0.5)'''


#2.movie ticket pricing system
'''n=int(input())
total=0
for _ in range(n):
    age=int(input())
    if age>=5 and age<=18:
        total+=100
    elif age>=19 and age <=60:
        total+=150
    elif age>60:
        total+=120
print(total)'''


#3.electricity bill generator
'''units=int(input())
bill=0
if units<=100:
    bill+=units*1.5
elif units>100 and units<=200:
    bill+=150+(units-100)*2.5
elif units>200 and units<=500:
    bill+=400+(units-200)*4
else:
    bill+=1600+(units-500)*6
print(float(bill))'''


#4.car parking fee calculator
'''hours=int(input())
days=hours//24
remaining_hours=hours%24
total_fee=days*200
if remaining_hours<=2:
    total_fee+=30
else:
    total_fee+=30+(remaining_hours-2)*10
print(total_fee)'''


#5.product inventory checker
'''name=input()
qua=int(input())
if qua==0:
    print("out of stock")
elif qua>0 and qua<10:
    print("low stock")
elif qua>11 and qua<50:
    print("in stock")
elif qua>50:
    print("overstock")'''


#6.pattern
'''n=int(input())
for row in range(n):
    for col in range(n):
        if (row+col)%2==0:
            print(0,end=' ')
        else:
            print(1,end=' ')
    print()'''


#6.3
'''n=int(input())
for row in range(n):
    for col in range(n):
        print((row+col)%2,end=' ')
    print()'''

#7.gym subscription billing
'''ch=int(input())
ppl=int(input())
if ch==1:
    print(ppl*500)
elif ch==2:
    print(ppl*1300)
elif ch==3:
    print(ppl*5000)
elif ch==0:
    exit()
else:
    print("invalid choice")'''

#8.billing bot
'''total=float(input())
if total<1000:
    print(total)
elif total>999 and total<5000:
    print(total-total*0.05)
elif total>4999 and total<10000:
    print(total-total*0.1)
elif total>=10000:
    print(total-total*0.15)'''

#9.atm pin verification
'''pin=1234
for _ in range(3):
    epin=int(input())
    if epin==pin:
        print("acess granted")
        break
else:
    print("atm blocked.try again later")'''

#10.bus booking system
'''total_seats=int(input())
booked_seats=list(map(int,input().split()))
print(f'total seats:{total_seats}')
print(f'booked: {len(booked_seats)}')
print(f'available: {total_seats-len(booked_seats)}')'''
