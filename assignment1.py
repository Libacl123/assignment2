a=[45,56,98,3,67,9,90]
max=a[0]
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
print("largest of array: ",max)