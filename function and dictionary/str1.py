user=input("Please input something:")

countup=0
countdo=0
for i in user:
    if 65<=ord(i)<=90:
        
        countup+=1
    else:
        countdo+=1
if countdo>=countup:
    print(user.lower())
else:
    print(user.upper())