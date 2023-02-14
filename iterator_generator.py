
# Ex 1
# def get_items():
#     yield 1

# val = get_items()
# # print(val)
# print(next(val))

# def get_items():
#     for i in range(1, 11):
#         yield i

# val = get_items()

# for i in val:
#     print(i)

# Ex 3

# def get_items():
#     for i in range(1,4):
#         yield i

# l = get_items()

# print(next(l))
# print(next(l))
# print(next(l))

# Ex.4

# number_list = [i for i in range(1, 101)]
# print(number_list)

# Ex 5

# number_list = (i for i in range(1, 101))
# for n in number_list:
#     print(n)

# Ex 6
# number_list = {i for i in range(1, 101)}
# print(number_list)

# Ex7

# number_list = {i: i**2 for i in range(1, 101)}
# print(number_list)

# Ex8

# numbers = (abs(x) for x in [-1, 0, 1])

# for i in numbers:
#     print(i)

# Ex9

# numbers = [abs(x) for x in [-1, 0, 1]]
# print(numbers)

# Ex 10

# number_list = (i for i in range(3, 31, 3))
# for n in number_list:
#     print(n)


# number_list = [i for i in range(3, 31) if i%3 == 0]
# print(number_list)


# number_list = [i for i in range(2, 1001) if i%2 == 0]
# print(number_list)



# Ex 3

# Find sum all elements of the list

# number_list = [1, '2',3,4,'5']
# number_list = [int(i) for i in number_list]

# print(sum(number_list))



# Ex. multiplication table


# numbers = [i for i in range(1, 10)]

# print('----+---------------------------------------------------------------------------')
# print('| x | ', end='\t')

# for n in numbers:
#     print(f'  {n}  ', end='\t')
# print('|')
# print('----+---------------------------------------------------------------------------')

# for i in numbers:
#     print(f'| {i} |', end='\t')
#     for j in numbers:
#         print(f'  {i * j:0>2d}  ', end='\t')
#     print('')

# print('----+---------------------------------------------------------------------------')
