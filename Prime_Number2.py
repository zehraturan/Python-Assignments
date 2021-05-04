n= int(input("which are between 1 to 100: "))

prime = []
for i in range(1,n+1) :
  if i == 2 :
    prime.append(i)       
  elif i % 2 :
    control = True
    if i == 1 :
      control = False
    else :
     j = 2
    while j < i / 2 :     
      if (i / j).is_integer() :          
        control = False
        break
      j+=1
    if control :
      prime.append(i)    

print(prime)