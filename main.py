def count_meals(file:str):
    with open(file, encoding='utf-8') as f:
        str_ = f.readlines()
        count = str_.count('\n')
    return count+1

def cooking(file:str):
    with open(file, encoding='utf-8') as f:
        cook_book = {}
        list_ingr = ['ingredient_name', 'quantity', 'measure']

        for count in range(count_meals(file)):
            name_meal = f.readline().strip()
            cook_book[name_meal] = []
            quantity_ingr = int(f.readline())
            for i in range(quantity_ingr):
                ingr = f.readline().strip().split(' | ')
                ingr[1] = int(ingr[1])
                dict_ingr = dict(zip(list_ingr, ingr))
                cook_book[name_meal] = cook_book[name_meal] + [dict_ingr]
            f.readline()
    return cook_book

print(cooking('Cookbook.txt'))

def get_shop_list_by_dishes(dishes, person_count):
    dict_ = cooking('Cookbook.txt')
    ingredients = {}
    for meal in dishes:
        if meal in dict_.keys():
            i = dict_[meal]
            for ingr in i:
                sorted_ingr = dict(sorted(ingr.items()))
                a = sorted_ingr['ingredient_name']
                del sorted_ingr['ingredient_name']

                sorted_ingr['quantity'] = sorted_ingr['quantity'] * person_count
                if ingr['ingredient_name'] not in ingredients.keys():
                    ingredients[a] = sorted_ingr
                else:
                    ingredients[a]['quantity'] += sorted_ingr['quantity']
    return print(ingredients)

print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))




