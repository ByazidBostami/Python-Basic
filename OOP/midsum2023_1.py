class CoffeeMachine:
    def __init__(self, brand_name):
        self.brand_name = brand_name
        self.ingredients = []

    def insertIngredients(self, *ingredients):
        self.ingredients.extend(ingredients)

    def getDetails(self):
        ingredients_str = ", ".join(self.ingredients)
        return f"Brand Name: {self.brand_name}\nIngredients: {ingredients_str}"

# Driver code
cm1 = CoffeeMachine("Miyako")
cm1.insertIngredients("Coffee beans", "Milk", "Sugar")
print(cm1.getDetails())
