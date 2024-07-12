
R_file=open (r"example.txt")
Cap_count=0
Low_count=0

for x in R_file.read():
    if x.isupper():
        Cap_count+=1
    if x.islower():
        Low_count+=1
print("Upper Letters Found :",Cap_count)
print("Lower Letters Found :",Low_count)



