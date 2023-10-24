def calc(x,y,oper):
  fun_operation = {
      '+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y,
      '%': lambda x, y: x % y,
      '^': lambda x, y: x ** y,
    }
  try:
    return fun_operation[oper](x, y)
  except KeyError:
    print("Invalid")
    return None

num1,oper,num2=input("Enter Str: ").split()
print(calc(int(num1),int(num2),oper))

