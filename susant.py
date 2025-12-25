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

#### while loop #######
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess:'))
    guess_count += 1
    if guess == secret_number:
        print('you won!')
        break
else:
    print('sorry, you failed')

    
command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is stopped")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print(""""
    start - to start the car
    stop - to stop the car
    quit - to quit
""")
    elif command =="quit":
        break
    else:
        print("sorry, I don't understand")

