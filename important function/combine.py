from functools import reduce
numbers = [1,2,3,4,5,6,7,8,9,10]

even_filters = list(filter(lambda n : n % 2 == 0 ,numbers))

print(even_filters)

square_even_number = list(map(lambda n : n*2, even_filters))

print(square_even_number)

sum_of_square = reduce(lambda x,y : x+y  ,square_even_number)

print(sum_of_square)