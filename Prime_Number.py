number = int(input("Enter the number: "))
if number > 1 :
    if number == 2 :
        print (f"{number} is a prime number")
    elif number % 2 :
        i = 2
        control = True
        while i < number :
            if (number / i).is_integer() :
                print (f"{number} is not a prime number")
                control = False
                break
            i+=1
        if control :
            print (f"{number} is a prime number")    
    else :
        print(f"{number} is not a prime number.")
else :
    print(f"{number} is not a prime number.")
