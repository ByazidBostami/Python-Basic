class Foodie:
    menu = {'Chicken Lollipop': 15, 'Beef Nugget': 20, 'Americano': 180, 'Red Velvet': 150, 'Prawn Tempura': 80, 'Saute Veg': 200}

    def __init__(self, name):
        
        self.name = name
        self.cart = []

    def show_orders(self):
        
        num_items = len(self.cart)
        items = ', '.join(self.cart)
        total_spent = self.calculate_total_spent()
        return f"{self.name} has {num_items} item(s) in the cart.\nItems: [{items}]\nTotal spent: {total_spent}."

    def order(self, *items):
        
        for item in items:
            item_name, quantity = item.split('-')
            self.cart.extend([item_name] * int(quantity))
            price_per_unit = self.menu[item_name]
            total_price = price_per_unit * int(quantity)
            print(f"Ordered - {item_name}, quantity - {quantity}, price (per Unit) - {price_per_unit}.")
            print(f"Total price - {total_price}")

    def pay_tips(self, tips=0):
        
        if tips > 0:
            print(f"Gives {tips}/- tips to the waiter.")
        else:
            print("No tips to the waiter.")

    def calculate_total_spent(self):
       
        total_spent = 0
        for item in self.cart:
            total_spent += self.menu[item]
        return total_spent



f1 = Foodie('Frodo')
print(f1.show_orders())
print('1----------------------')
f1.order('Chicken Lollipop-3', 'Beef Nugget-6', 'Americano-1')
print('2----------------------')
print(f1.show_orders())
print('3----------------------')
f1.order('Red Velvet-1')
print('4----------------------')
f1.pay_tips(20)
print('5----------------------')
print(f1.show_orders())
f2 = Foodie('Bilbo')
print('6----------------------')
f2.order('Prawn Tempura-6', 'Saute Veg-1')
print('7----------------------')
f2.pay_tips()
print('8----------------------')
print(f2.show_orders())
