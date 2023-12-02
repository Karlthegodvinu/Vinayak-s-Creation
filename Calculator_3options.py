print("**********CALCULATOR**********")
import math
x=math.pi

print("1. Basic Math \n2. Trigonometry \n3. Multiplication Table \n4. Factorial")

n=int(input("Enter the value of n: "))

if n==1:
    print("1.Addition \n2.Subsraction \n3.Product \n4.Division")
    a=int(input("Enter the value: "))

    c=int(input("Value of the 1st number: "))
    d=int(input("Value of the 2nd numnber: "))
    if a==1:
        x=c+d
        print(f"Addition of {c} and {d} is {x}")
    elif a==2:
        x=c-d
        print(f"Substraction of {c} and {d} is {x}")
    elif a==3:
        x=c*d
        print(f"Product of {c} and {d} is {x}")
    elif a==4:
        x=c/d
        print(f"Division of {c} and {d} is {x}")
    else:
        print("There is no option like that")

elif n==2:
    print("1. sin \n2. cos \n3. tan \n4. cosec \n5. sec \n6. cot")

    c=int(input("Enter the value: "))


    a=int(input("Enter the value of c is the numerator : "))
    b=int(input("Enter the value of d is the denominator : "))
    if c==1:
        sin=math.sin(a*x/b)
        print(format(sin,'.2f'))
    elif c==2:
        cos=math.cos(a*x/b)
        print(format(cos,'.2f'))
    elif c==3:
        tan=math.tan(a*x/b)
        print(format(tan,'.2f'))
    elif c==4:
        cosec=1/math.sin(a*x/b)
        print(format(cosec,'.2f'))
    elif c==5:
        sec=1/math.cos(a*x/b)
        print(format(sec,'.2f'))
    elif c==6:
        cot=1/math.tan(a*x/b)
        print(format(cot,'.2f'))
    else:
        print("There is no option like that")

elif n==3:
    num=int(input("Enter the number whose table is to be given : "))
    for i in range(1,11):
        print(num,' x ',i,' = ',num*i)
elif n==4:
    a=int(input("Enter the value for calculating Facotrial: "))
    def factorial(a):
        if a==0:
            return 1
        else:
            return a* factorial(a-1)

    result=factorial(a)
    print(f"The factorial of {a} is {result}")

else:
    print("There is no option like that")
    
        
        
        
