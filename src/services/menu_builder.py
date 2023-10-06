from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        main_menu = list()
        print("bode", self.inventory)
        for dish in self.menu_data.dishes:
            menu = {
                "dish_name": "",
                "ingredients": "",
                "price": "",
                "restrictions": "",
            }
            if not restriction:
                menu["restrictions"] = dish.get_restrictions()
                menu["ingredients"] = dish.get_ingredients()
                menu["dish_name"] = dish.name
                menu["price"] = dish.price
                main_menu.append(menu)
            elif restriction not in dish.get_restrictions():
                menu["restrictions"] = dish.get_restrictions()
                menu["ingredients"] = dish.get_ingredients()
                menu["dish_name"] = dish.name
                menu["price"] = dish.price
                main_menu.append(menu)

        return main_menu
