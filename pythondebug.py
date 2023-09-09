import pdb

def add_numbers(a, b):
    result = a + b
    pdb.set_trace()
    return result

x = 5
y = 7
result = add_numbers(x, y)
print(result)