num=[45, 73, 105, 7, 54, 80]

sum = []
for n in num:
  s= 0
  while n > 0:
    digit = n%10
    s+= digit
    n //= 10
  sum.append(s)
print("sum of digits in a list :",sum)  