import math
#6k+-1
def isPrime(num):
  if(num <= 1): return False
  if(num == 2 or num == 3): return True
  if(num % 2 == 0 or num % 3 == 0): return False

  sqrtOfNum = math.ceil(math.sqrt(num))
  #k=6
  for i in range(5, sqrtOfNum, 6):
    if(num % i == 0 or num % (i+2) == 0):
      return False
  return True

#factor <= sqrt num
largeNum = 600851475143 
primeList = []
sqrtOfLargeNum = math.ceil(math.sqrt(largeNum))
for i in range(1, sqrtOfLargeNum, 2):
  if(largeNum % i == 0):
    if(isPrime(i)):
      primeList.append(i)
    otherFactor = largeNum/i
    if(isPrime(otherFactor)):
      primeList.append(otherFactor)

primeList.sort()
print(primeList)
  

