def find_num_cakes(recipe, available):
    return min(available.get(item, 0)//recipe[item] for item in recipe)
