No=int(input("Enter Any Number"))
Sum=0
while No!=0:
    rem=No%10
    Sum=Sum+rem
    No=No//10
print("Sum Of Digits = ", Sum)    
