givenlist=["hey", "there", "", "what's", "", "up", "", "?"]
print(f'Original list:{givenlist}')
mylist=[]
for i in givenlist:
    if i!="":
        mylist.append(i)
print(f"Modified list{mylist}")