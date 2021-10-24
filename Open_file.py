import os


def create_menu():
    path = os.path.join(os.getcwd(), 'Cook_book1.txt')

    with open(path, 'r', encoding='utf-8') as file:
        cook_book = {}
        for dish in file:
            dish_name = dish.strip()
            counter = int(file.readline().strip())
            temp_data = []
            for item in range(counter):
                ingredients, quantity, unit =file.readline().split('|')
                temp_data.append(
                    {'ingredients': ingredients, 'quantity': quantity, 'unit': unit}
                )
            cook_book[dish_name] = temp_data
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = create_menu()
    list_ingr = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for val in cook_book[dish]:
                if val['ingredients'] in list_ingr.keys():
                    list_ingr[val['ingredients']] = {'measure': val['unit'],
                                                     'quantity':  list_ingr[val['ingredients']]['quantity'] + int(val['quantity']) * person_count}
                else:
                    list_ingr[val['ingredients']] = {'measure': val['unit'], 'quantity': int(val['quantity']) * person_count}
        else:
            print(dish, ' в нашем меню нет!')
    print(list_ingr)


get_shop_list_by_dishes(['Омлет', 'суп'], 2)
