maxValue = 4000000

def fib(num1, num2):
  num3 = num1+num2
  if(num3 > maxValue):
    return 0
  if(num3 % 2 == 0):
    #even. Add the number to the return and get the next number
    return num3 + fib(num2, num3)
  else:
    #odd
    return fib(num2, num3)

#1,2
total = fib(1,2)
total += 2
print(total)
