def leap_year(year) :
  if year % 4 != 0:
    print(f"{year} is not a leap year")
  else :
    if year % 400 == 0:
      print(f"{year} is a leap year")
    elif year % 100 ==0 :
      print(f"{year} is not a leap year")
    else:
      print(f"{year} is a leap year")

year = int(input("Enter a year for calculating if it is a leap year or not: "))
leap_year(year)