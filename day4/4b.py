result = 0
for n in range(236491,713787):
  digits = [int(x) for x in list(str(n))]
  adjacent = False
  increase = False
  if digits == sorted(digits):
    increase = True

  for d in digits:
    if digits.count(d) == 2:
      adjacent = True
      break
  if adjacent and increase:
    result += 1
print(result)