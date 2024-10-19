def cakes(recipe, available):
    if not all([key in available for key in recipe]):
        return 0
    return min([available[key] // value for key, value in recipe.items()])
