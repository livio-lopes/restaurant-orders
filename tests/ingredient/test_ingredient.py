from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_tomate = Ingredient("tomate")
    ingredient_batata = Ingredient("batata")

    assert ingredient_tomate == Ingredient("tomate")
    assert ingredient_batata != Ingredient("tomate")
    assert hash(ingredient_batata) != hash(ingredient_tomate)
    assert hash(ingredient_tomate) == hash(Ingredient("tomate"))
    assert repr(ingredient_tomate) == "Ingredient('tomate')"
    assert ingredient_tomate.name == 'tomate'
    assert len(ingredient_tomate.restrictions) == 0
