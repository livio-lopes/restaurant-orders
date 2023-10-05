from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("batata frita", "bode")
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("batata frita", -1)
    prato_paraense = Dish("peixe com açai", 29.90)
    assert repr(prato_paraense) == "Dish('peixe com açai', R$29.90)"
    assert prato_paraense.name == "peixe com açai"
    assert prato_paraense.price == 29.90
    prato_mineiro = Dish("feijão tropeiro", 17.90)
    assert prato_paraense == Dish("peixe com açai", 29.90)
    assert prato_paraense != prato_mineiro
    assert hash(prato_paraense) == hash(Dish("peixe com açai", 29.90))
    assert hash(prato_paraense) != hash(prato_mineiro)
    prato_paraense.add_ingredient_dependency(Ingredient("dourada"), 2)
    prato_paraense.add_ingredient_dependency(Ingredient("açai"), 1)
    prato_paraense.add_ingredient_dependency(
        Ingredient("farinha de tapioca"), 1
    )
    assert len(prato_paraense.recipe) == 3
    assert len(prato_paraense.get_ingredients()) == 3
    assert len(prato_paraense.get_restrictions()) == 0
