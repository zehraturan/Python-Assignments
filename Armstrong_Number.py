number = input("Enter a number: ").strip()
if number.isdigit() :
    l_number = list(number)
    result = 0
    for i in l_number :
        result += int(i) ** len(l_number)
    
    if result == int(number) :
        print("{} is an Armstrong number".format(number))
    else : 
        print("{} is not an Armstrong number".format(number)) 
else :
    print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")