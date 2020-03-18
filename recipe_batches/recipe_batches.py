#!/usr/bin/python

import math
import os

os.system("clear")


def recipe_batches(recipe, ingredients):
    if len(ingredients) != len(recipe):
        return 0

    ing_count = []

    for rec, ing in zip(recipe.items(), ingredients.items()):
        ing_count.append(ing[1] // rec[1])

    return min(ing_count)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
