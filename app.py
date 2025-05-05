# A Simple Calculator app with functions

def add(num1, num2):
  return num1 + num2

def sub(num1, num2):
  return num1 - num2

def div(num1, num2):
  if num2 == 0:
    return 'cannot dive by zero!'
  else:
    return num1 / num2

def multi(num1, num2):
  return num1 * num2

# Display
print('Welcome to Simple Calculator')
print('You can do the basic calculations')

# Take input
n1 = int(input('Enter First Number: '))
op = input(' Enter "+" or "-" or "*" or "/" only: ')
n2 = int(input('Enter First Number: '))
  
if op == '+':
  result = add(n1, n2)
  
elif op == '-':
  result = sub(n1, n2)
  
elif op == '*':
  result = multi(n1, n2)
  
elif op == '/':
  result = div(n1, n2)
else:
  print('Enter correct op')
print(f'The calculated result is: {result}')
