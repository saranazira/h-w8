# Ex 1. Filter

# my_list = [1,5,3,7,4,8,10,32,435,56,132]

# print(f'Ishodniy spisok: {my_list}')

# new_list = list(filter(lambda x: x % 2 == 0, my_list))

# print(f'Otfiltrovanniy spisok: {new_list}')

### # new_list = list(filter(lambda 1: 1 % 2 == 0, my_list))
### # new_list = list(filter(lambda 5: 5 % 2 == 0, my_list))
### # new_list = list(filter(lambda 3: 3 % 2 == 0, my_list))


# Ex 2. Map

# my_list = [4,2,6,3,7,9,34,23,56,78,779]
# print(f'Ishodniy spisok: {my_list}')

# new_list = list(map(lambda x: x**2, my_list))
# print(f'Vozvedenie vo vtoruyu stepen: {new_list}')


# Ex 3. Reduce

# my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# result = 0 

# for n in my_list:
#     result += n
# print(result)

# Ex. reduce different way

# from functools import reduce

# my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# result = reduce(lambda acc, x: acc + x, my_list)

# print(result)

# Ex. cities

# Есть список [‘MOSKOW’, ‘BISHKEK’, ‘ALMATY’, ‘BERLIN’, ‘ANKARA’, ‘AMSTERDAM’],
# преоброзовать названия в списке в нижний регистр применяя исключительно фукцию map,
# если хотите можете применить lamba функцию тоже, но можно обойтись и без него.

# cities = ['MOSKOW', 'BISHKEK', 'ALMATY', 'BERLIN', 'ANKARA', 'AMSTERDAM']
# new_list = list(map(lambda name: cities.lower()))
# print(new_list)

# Ex. 

# # Отфильтруйте отобрав в новый список только четные числа
# # [4, 3, 6, 8, 9, 7, 1, 2, 34, 5, 56, 76], и возведите в в третью
# # степень каждую цифру отфильтрованного списка.

# nums = [4, 3, 6, 8, 9, 7, 1, 2, 34, 5, 56, 76]
# new_list = list(map(lambda n: n**3), filter(lambda n: n % 2 == 0, nums))
# print(new_list)

# Вычислите сумму элементов списка [34, 5, 23, 68, 56, 890, 123, 564],
# но перед этим отфильтровать только нечетные числа.

# from functools import reduce
# nums = [34, 5, 23, 68, 56, 890, 123, 564]
# result = reduce(lambda x, y: x+y, filter(lambda n: n % 2 != 0, nums))
# print(result)

# Ex.

courses_info = [
    {
    'id':'Python',
    'name': 'Python course',
    'duration': '6 months',
    'time':'Mo, Thur, Sat 19:00-21:00',
    'price': 10000,
   
    'id':'JS',
    'name': 'JS course',
    'duration': '3 months',
    'time':'Mo, Tu, Sat 19:00-21:00',
    'price': 10000,
   
    }
    
    ]
print('Codify courses')
for item in courses_info:
    print('--------------------------------------------')
    # print(f"Name of the course: {item['name']}")
    # print(f"Duration of the course: {item['duration']}")
    # print(f"Time: {item['time']}")
    # print(f"Price: {item['price']}")
    print(f"Programming language: {item['id']}")

    print('--------------------------------------------')

while True:
    name = input('Choose programming language:')
    info = list(filter(lambda x: x['name'] == name.lower, courses_info))

    if not courses_info:
        print('this is course is not exist!')
        continue
    break

print(info)