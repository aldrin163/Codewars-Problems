def cakes(recipe, available):
    return min(available.get(i,0)//recipe.get(i) for i in recipe)