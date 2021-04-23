age = input("Are you a cigarette addict older than 75 years old? ").strip().title()
chronic = input("Do you have a severe chronic disease ?").strip().title()
immune = input("Is your immune system too weak? Variable ").strip().title()

if age == "No" and chronic == "No" and immune == "No":
     print("You are not in risky group")
else :
      print("You are in risky group")