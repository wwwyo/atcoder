a, b = map(int, input().split())
code = ''
if a < b:
  code = '<'
elif a > b:
  code = '>'
else:
  code = '=='

print("a {} b".format(code))