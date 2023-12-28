#Maths relating functions
from math import sin,cos,tan,asin,radians,degrees,atan

def hcm(a,b):
    loopvariable = max(a,b)
    while loopvariable:
        if a%loopvariable==0 and b%loopvariable==0:
            print("HCF is: ",loopvariable)
            break
        else: loopvariable = loopvariable-1

def lcm(a,b):
    loopvariable = min(a,b)

    while loopvariable:
        if loopvariable%a == 0 and loopvariable%b==0:
            print("LCM is: ", loopvariable)
            break
        else: loopvariable += 1

def split_in(one,two,three):
    y=one*three
    if y<0:
      increment = -1
    else: increment = 1

    for m in range(-y, y+1,increment):
        if m != 0 and y % m == 0:
            n = y // m
            if m + n == two:
                print(f"{two} can be split into {m}+{n}")
                break
            else: 
              continue
            
        else: 
          continue  
    else:
        print("No integer pair found.")

def collatz(num):
    while num:
        while num %2 == 1:
          num = num*3+1
          print(num)
        while num %2 ==0:
          num = num//2
          print (num)
        if num == 1:
          break
        
    print("*The pattern of 4 , 2 , 1 now continues forever.")


def factorial2(n):
   if n == 1:
      return 1
   return n*factorial2(n-1)

def trig(angle):
  try:
    v = radians(angle)  # Convert angle to radians
  except:
     print("Input should be a valid angle in degrees.")
     

  sinValue = round(sin(v),3)
  cosValue = round(cos(v),3)
  tanValue = round(tan(v),3)


  print(f'Sin: {sinValue}, Cos: {cosValue}, Tan: {tanValue}')
  print(round(degrees(asin(sin(v)))))
  print(degrees(atan(1)))


def factorial(num):
  i=1
  for w in range (1,num+1):
      i = i*w
  print(i)

def fibionacci_series(num):
  a = 0
  b = 1
  series = 0

  print("Printing Fibionacci Series")
  for __i__ in range(num):    
          a = b
          b = series
          series = a + b
          print(series)