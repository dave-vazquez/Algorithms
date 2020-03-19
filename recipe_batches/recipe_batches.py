#!/usr/bin/python

import math
import os

os.system("clear")


def recipe_batches(recipe, ingredients):
    # check for equal sets of ingredients
    if len(ingredients) != len(recipe):
        return 0

    ing_count = []

    # loop through both recipes and ingredients simultaneously
    for rec, ing in zip(recipe.items(), ingredients.items()):
        # append the number of quantities for each recipe ingredient
        # that can be made using the quantity of each ingredient available
        ing_count.append(ing[1] // rec[1])

    # return the smallest count in the ingredients count to represent
    # the minimum amount of servings for each recipe that can be made.
    # ...if it's any other number or the max, you run the risk of not
    # being able to make the number of servings without running out of
    # an ingredient with less serving quantities available
    return min(ing_count)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
