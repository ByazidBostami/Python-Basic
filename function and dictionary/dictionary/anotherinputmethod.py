user = input("Please enter a dictionary (e.g., 'key1:value1, key2:value2'): ")

check_pairs = user.split(",")

my_dictionary = {}

for p in check_pairs:

    key_value = p.strip().split(":")

    if len(key_value) == 2:
        key = key_value[0].strip()
        value = int(key_value[1].strip()) #Strip any extra whitespace and split each pair into key and value
        
        my_dictionary[key] = value

print(my_dictionary)