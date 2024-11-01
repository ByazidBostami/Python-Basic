# user = input("Please input something with comma :")

# mytuple = tuple(user.split(","))
# print(mytuple)


user = int(input("Please input how many tuple you want to calculate :"))

check_list = []

for i in range(user):
    tup = int(input())
    check_list.append(tup)

mytuple = tuple(check_list)

if len(mytuple) == 2:
    print("not possible")
else:
    print(mytuple[2:len(mytuple)-2:1])  #tuple[start:stop:step]

