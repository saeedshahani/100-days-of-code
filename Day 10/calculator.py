from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  calc_loop = "y"
  num1 = float(input("What's the first number?: "))
  while calc_loop == "y":
    for operation in operations:
      print(operation)
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    calc_loop = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.:")
    if calc_loop == "y":
      num1 = answer
    else:
      calc_loop =="n"
      clear()
      calculator()
    
calculator()