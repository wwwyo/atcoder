import string
import sys
list = ""
for line in sys.stdin:
    list += line.lower()
for s in string.ascii_lowercase:
    print("{} : {}".format(s, list.count(s)))

import sys

cnt = {}

for line in sys.stdin:
  for l in line:
    if l.isalpha():
      c = l.lower()
      cnt[c] = cnt.get(c,0)+1

for i in range(26):
  c = chr(ord('a')+i)
  print( c, " : ", cnt.get(c,0), sep = '' )