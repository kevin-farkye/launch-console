print("Hello there, fellow programmer!")
name = input("What is your name? ")
print(f"Nice to meet you, {name}. Welcome to the Launch Console!")



program = True
while program:
  print("Pick one of the following options to learn about me: ")
  print("1. About Me")
  print("2. My Goals")
  print("3. Education")
  print("4. Exit")
  choice = input('')


  if choice == "1":
    print("My name is Kevin. I am a 15 (almost 16) year old senior from Greensboro, NC.")
  elif choice == "2":
    print("I want to become a mechanical engineer. I am learning Pyhton to help me build knowledge and gain experience.")
  elif choice == "3":
    print("I have earned a certificate in AutoDesk AutoCAD from my Drafting I class, and I am going to earn an AutoDesk Inventor certificate from my Drafting II class at the end of the school year.")
  elif choice == "4":
    print("Goodbye!")
    program = False
  else:
    print("Please choose a number 1-4.")
