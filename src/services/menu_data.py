from models.dish import Dish, Ingredient
import csv

# Req 3


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        with open(source_path) as file:
            headers, *rows = csv.reader(file)
            for row in rows:
                instance = Dish(row[0], float(row[1]))
                instance.add_ingredient_dependency(
                    Ingredient(row[2]), int(row[3])
                )
                self.dishes.add(instance)


# test = MenuData("data/menu_base_data.csv")
# print(test.dishes)
