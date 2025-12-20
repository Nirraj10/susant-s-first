#name, price, qty = 'soap', 19.99, 5
#print(name, price,qty)

#type of variables
#a = 15
#print(type(a))

#a = 12.75
#print(type(a))

#a = 'john'
#print(type(a))

#a = [11, 12, 13, 14 ,15]
#print(type(a))

x = 123
y = 93939479357975957
print (x)
print (y)
import sys
sys.getsizeof(x)

x = 101
x = 205

print(x)
id(x)
c = complex(5, 3.1)
print(c)

name1 = 'susant'
name2 = "susant"
name3 = '"susant"'
print(name1, name2, name3)

length = 15
breadth = 5
area = length * breadth
print('Area:' , area)

length = int(input('Enter Length'))
breadth = int(input('Enter Breadth'))
area = length * breadth
print('Area' , area)

n = int(input('Enter a Number'))
if n%2 ==0:
    print('Even')
else:
    print('odd')

age = int(input('Enter age'))
if age >=18 and age <=60:
    print('can work')
else:
    print('cannot work')

maths = int(input('Enter Maths Marks'))
physics = int(input('Enter physics mark'))
chemistry = int(input('Enter chemistry marks'))
if maths >= 45 and physics >= 45 and chemistry >= 45:
    print('passed')
else:
    print('failed')


amount = int(input ('Enter bill Amount'))
if amount <1000:
    total = amount-amount*0.1
elif amount >= 1000 and amount <5000:
    total = amount-amount*0.15
elif amount >= 5000 and amount <10000:
    total = amount-amount*0.2
else:
    total = amount-amount*0.25
print('pay:', total)

dayNo = int(input('Enter a Day Number'))
if dayNo == 0:
    print('Monday')
elif dayNo == 1:
    print ('Tuesday')
elif dayNo == 2:
    print('Wednesday')
elif dayNo == 3:
    print('Thursday')
elif dayNo == 4:
    print('Firday')
elif dayNo == 5:
    print('Saturday')
elif dayNo == 6:
    print('Sunday')
else:
    print('Invalid Day Number')
    
digit = int(input('Enter a number'))
if digit == 0:
    print('zero')
elif digit == 1:
    print('one')
elif digit == 2:
    print('two')
else:
    print('Invalid No')


year = int(input('Enter a year'))
if year % 100 == 0:
    if year % 400 == 0:
        print('Leap year')
    else:
        print('Not a Leap year')
elif year % 4 == 0:
    print('Leap year')
else:
    print('not leap year')


s1 = 'software'
s2 = 'Hardware'

s1 > s2
