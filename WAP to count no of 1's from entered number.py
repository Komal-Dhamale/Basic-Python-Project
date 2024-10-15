No=int(input("Enter Any Number"))
Count=0
while No>0:
    rem=No%10
    if rem==1:
        Count=Count+1
    No=No//10
print("Count Of 1's From Entered No = ", Count)    
