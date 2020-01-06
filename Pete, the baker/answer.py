def cakes(recipe, available):
    min = float('inf')
    for i in recipe:
        if i in available:
            num = available.get(i)//recipe.get(i)
            if num < min:
                min = num
        else:
            return 0
    return min