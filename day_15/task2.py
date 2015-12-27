from ingredient import Ingredient
from input_data import input_data
from utils import generate_divisions


def solution():
    ingredients = [Ingredient.parse_line(line) for line in input_data]
    max_score = -float('inf')
    for ratios in generate_divisions(100, len(ingredients)):
        sum_ingredients = Ingredient.empty_ingredient()
        for ingredient, ratio in zip(ingredients, ratios):
            sum_ingredients += ingredient.get_amount(ratio)

        if sum_ingredients.calories == 500:
            score = sum_ingredients.get_full_score()
            if score > max_score:
                max_score = score
    return max_score
