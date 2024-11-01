user = int(input("Please type how many tuple you want to calculate: "))

mylist = []
for i in range(user):
    inp = int(input())
    mylist.append(inp)

mytuple = tuple(mylist)

user_two = int(input("Please input a number to check: "))

count = 0

for i in range(len(mytuple)):
    if user_two == mytuple[i]:
        count+=1

print(f"{user_two} appears {count} times in the tuple")

