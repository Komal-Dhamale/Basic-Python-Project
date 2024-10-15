No=int(input("Enter Any Number"))
Even=0
Odd=0
while No!=0:
    rem=No%10
    if rem%2==0:
        Even=Even+1
    else:
        Odd=Odd+1
    No=No//10
print("Even Digits = ", Even)
print("Odd Digits = ", Odd)
