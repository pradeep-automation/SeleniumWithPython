# import pdb
#
# def add_numbers(a, b):
#     result = a + b
#     pdb.set_trace()
#     return result
#
# x = 5
# y = 7
# result = add_numbers(x, y)
# print(result)

ls = [1,2,3,[4,5]]
ls1 = ls.copy()
ls1[0] = 5
print(ls1)
print(ls)

list1 = [{"name": "pradeep", "age": 34},{"name": "wramola", "age": 40}]
# for item in list1:
    # for k, v in item.items():
    #     print(k, v, end = " ")
    # # print("\n")

for item in list1:
    print(f"{item['name']} and {item['age']}")


