string="900009" # initial string

l = []
num1 = 999
num2 = 999
for i in range(num1, 100, -1):
  for j in range(i, 100, -1):
    string = str(i*j)
    stringlength=len(string) # calculate length of the list
    slicedString=string[stringlength:2:-1] # slicing 
    frontString = string[0:3]
    if(frontString == slicedString):
      l.append(i*j)
      print(i*j, ' : ', i, ':',j)

l.sort()
print(l)
