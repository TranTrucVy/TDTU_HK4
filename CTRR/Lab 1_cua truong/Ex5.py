def calc(a,b,operator):
  if operator == '+':
    return a+b
  elif operator == '-':
    return a-b
  elif operator == '*':
    return a*b
  elif operator == '/':
    return a/b
  else:
    return "Error"


num1,operator,num2=input("Enter string: ").split()
print(calc(int(num1),int(num2),operator))
