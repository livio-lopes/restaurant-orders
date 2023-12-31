from models.dish import Dish, Ingredient
import csv

# Req 3


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.__list_dishes = list()
        with open(source_path) as file:
            headers, *rows = csv.reader(file)
            for row in rows:
                instance = Dish(row[0], float(row[1]))
                if instance not in self.__list_dishes:
                    instance.add_ingredient_dependency(
                        Ingredient(row[2]), int(row[3])
                    )
                    self.__list_dishes.append(instance)
                else:
                    for dish in self.__list_dishes:
                        if dish == instance:
                            dish.add_ingredient_dependency(
                                Ingredient(row[2]), int(row[3])
                            )
        self.dishes = set(self.__list_dishes)

