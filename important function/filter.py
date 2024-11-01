def is_even(number):
    
    return number%2 == 0

numbers=[1,2,3,4,5,6,7,8,9,10]

even_number = filter(is_even,numbers)

print(list(even_number))