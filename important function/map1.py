def mapfun(x):
    return (x * 5) + 30 
list1=[1,2,3,5,454,45,2]

calculate_map = map(mapfun,list1)
print(list(calculate_map))