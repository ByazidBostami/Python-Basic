user = input("Please input something with comma : ")

mytuple = tuple(user.split(","))

final_tuple = ()

for i in range(len(mytuple)-1,-1,-1):
    final_tuple += (mytuple[i],)

print(final_tuple)
    
