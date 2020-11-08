import regex

rx = r'(\d)\1{+,}(*SKIP)(*F)|(\d)\2'
L = range(236491,713788)
count = 713788 - 236491

for n in L:
  digit = [int(i) for i in list(str(n))]
  if  digit != sorted(digit) or not bool(regex.search(rx, str(n))):
    count -= 1
print(count)