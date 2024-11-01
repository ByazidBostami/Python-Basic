user = int(input("How many element you want to add? "))
my_dictionary = {}

for i in range(user):
    keys = input("Please input keys:")
    value = int(input("Please input values: "))

    my_dictionary[str(keys)] = int(value)

sum = 0
avg = 0
for k,v in my_dictionary.items():
    sum += v
    avg = sum/user

print(f"Average is {int(avg)}")
