def calc(x,y,operator):
  operations = {
      '+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y,
      '%': lambda x, y: x % y,
      '^': lambda x, y: x ** y,
    }
  try:
    return operations[operator](x, y)
  except KeyError:
    print("Invalid operator")
    return None

num1,operator,num2=input("Enter string: ").split()
print(calc(int(num1),int(num2),operator))

