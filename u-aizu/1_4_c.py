a, op, b = input().split()

while op != "?":
  if op == "+":
    print(int(a) + int(b))
  elif op == "-":
    print(int(a) - int(b))
  elif op == "*":
    print(int(a) * int(b))
  elif op == "/":
    print(int(a) // int(b))
  a, op, b = input().split()