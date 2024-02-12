string= "Grassisgreenerontheotherside"
print ("string entered is : " ,string)
dict= {}
for i in string:
     if i in dict:
          dict[i] += 1
     else:
          dict[i] = 1
res = max(dict, key = dict.get)
print ("Most repeating letter is " ,str(res))
