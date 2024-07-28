def print_params(a = 1, b="строка", c = True):
    print(a, b, c)

print_params(1,2,3)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

value_list = [{"a": 1, "b": 2}, "stroka", [15, 20]]
values_dict = {"a": 12, "b": [100, 250], "c": "nestroka"}

print_params(*value_list)
print_params(**values_dict)

values_list_2 = [1, "perec"]
print_params(*values_list_2, 42)
