# def outer_function():
#     def inner_function():
#         return "Hello from vitorer function"
#     return inner_function()
# print(outer_function())

def outer_function(name):
    def inner_function():
        return f"Hello from {name} function"
    return inner_function()

print(outer_function("Byazid"))
