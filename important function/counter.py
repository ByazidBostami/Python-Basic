#make a counter using clouser
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
count1 = make_counter()
print(count1())
print(count1())
print(count1())
print(count1())