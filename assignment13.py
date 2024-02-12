data = [34, "word", 4.5, "code", 89, 9.0]
dict= {}
for i in data:
  data_type = type(i).__name__
  if data_type in dict:
    dict[data_type].append(i)
  else:
    dict[data_type] = [i]
print(dict)
