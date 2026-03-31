# for i in range(2):
#     for j in range(5):
#         print(i, j, end=" ")

my_list_compr = [(i, j) for i in range(2) for j in range(5)]
my_list_alt = [[i + j for i in range(2)] for j in range(5)]
print(my_list_compr)
print("type of my_list_compr", type(my_list_compr))
print(my_list_alt)
print("type of my_list_alt", type(my_list_alt))

another_list_compr = [
    num**3 if num % 2 != 0 else "even" for num in range(1, 11)
]
print(another_list_compr)
