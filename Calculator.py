def add(a,b):
    return (a+b)

def sub(a,b):
    return (a-b)

def mult(a,b):
    return (a*b)

def pow(a,b):
    return (a**b)

def rem(a,b):
    if b!=0:
        return (a%b)
    else:
        print('Denominator should not be equal to 0')

def div(a,b):
    if b!=0:
        return (a/b)
    else:
        print('Denominator should not be equal to zero ')


print('This is simple arthematic calculator that consists of finding:\nSum of two numbers\nDifference between two numbers\nProduct of two numbers\nPower to some base\nRemainder of two numbers\nDivision of two numbers')
print()
print('For addition you have to use: +\nFor subtraction you have to use: -\nFor multiplication you have to use: x\nfor finding the value of some power to the base: ^\nFor remiander: %\nFor division: /')
print()

while True:
    Num1=int(input('Enter any number: '))
    Operation=(input('Enter any operation: '))
    Num2=int(input("Enter another number: "))

    if Operation=='+':
        print (f'The sum of {Num1} and {Num2} is:', add(Num1,Num2))

    elif Operation=='-':
        print(f'the difference of {Num1} and {Num2} is:', sub(Num1,Num2))

    elif Operation=='x':
        print(f'The product of {Num1} and {Num2} is:', mult(Num1, Num2))

    elif Operation=='^':
        print(f'The exponent {Num2} to the base {Num1} is equal to:', pow(Num1, Num2))

    elif Operation=='%':
        print(f'The remainder when {Num1} is divided by {Num2} is:', rem(Num1, Num2))

    elif Operation=='/':
        print(f'When {Num1} is divided by {Num2}:', div(Num1, Num2))

    else:
        print('Enter correct operation')
        break