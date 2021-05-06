n = 100
numstr = ""
for i in range(1,n+1) :
  if i % 3 == 0 and i % 5 == 0:
    numstr += "FizzBuzz" + "-"
  elif i % 3 == 0 :
    numstr += "Fizz" + "-"
  elif i % 5 == 0 :
    numstr += "Buzz" + "-"
  else :
    numstr += str(i) + "-"

print(numstr.strip('-'))