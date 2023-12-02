print("**********TRIGONOMETRIC CALCULATOR**********")
import math
x=math.pi

print("1. sin \n2. cos \n3. tan \n4. cosec \n5. sec \n6. cot")

c=int(input("Enter the value of c : "))


a=int(input("Enter the value of a is the numerator : "))
b=int(input("Enter the value of b is the denominator : "))
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
        
    



    
    

