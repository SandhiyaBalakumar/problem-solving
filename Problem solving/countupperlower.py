
R_file=open (r"example.txt")
Cap_count=0
Low_count=0
Alpha_count=0
Digit_count=0
Space_count=0

for x in R_file.read():
    if x.isupper():
        Cap_count+=1
    if x.islower():
        Low_count+=1
    if x.isalpha():
        Alpha_count+=1   
    if x.isdigit():
        Digit_count+=1   
    if x.isspace():
        Space_count+=1    
print("Upper Letters Found :",Cap_count)
print("Lower Letters Found :",Low_count)
print("Alphabetics Found :",Alpha_count)
print("Digits Found :",Digit_count)
print("Spaces Found :",Space_count)




