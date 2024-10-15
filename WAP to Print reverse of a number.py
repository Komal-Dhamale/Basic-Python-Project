No=int(input("Enter Any Number"))
rev=0
while No!=0:
    rem=No%10
    rev=rev*10+rem
    No=No//10
print("Reverse Number = ", rev)    
