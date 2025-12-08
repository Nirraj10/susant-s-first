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