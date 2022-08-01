#Simple Python Calculator

#function for calculations
def select_operation(a, b):
  user = input(str("Enter an Operation : "))
  if user == "+":
    print(float(a) + float(b))
  elif user == "-":
    print(float(a) - float(b))
  elif user == "*":
    print(float(a) * float(b))
  elif user == "/":
    print(float(a) / float(b))
  elif user == "%":
    print(float (a) % float(b))
  elif user == "**":
    print(float (a) ** float(b))
  else:
    print("Invalid Number") 
    return(float(a, b))

#function for instructions
def print_instructions():
  print("Simple Python Calculator")
  print("************************")
  print("\nOperation Symbols")
  
  a = [
    ["Sum = +", "Subtract = -", "Multiply = *"],
    ["Divison = /","Remainder = %","Power = **"]
  ]

  for row in a:
    for col in row:
      print(col)

#main
print_instructions()

try:
  first_number = float(input("\nEnter First Number : "))
  second_number = float(input("Enter Second Number : "))
except:
  print("Invalid number")

select_operation(float(first_number), float(second_number))


