user=input("Please input Something:")
a=True
c=True

for i in user:
    if  not i.isdigit():
        c=False
    if  not i.isalpha():
        a=False
    
if a==True:
    print("WORD")
if c==True:
    print('NUMBER')
else:
    print("Mixed")