def check_string_type(input_string):
    is_number = True
    is_word = True

    for char in input_string:
        if not char.isdigit():
            is_number = False
        if not char.isalpha():
            is_word = False

    if is_number:
        print("NUMBER")
    elif is_word:
        print("WORD")
    else:
        print("MIXED")

# Example usage:
input_str = input("Enter a string: ")
check_string_type(input_str)
