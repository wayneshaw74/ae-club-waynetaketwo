
def is_even(x):
    return x % 2 == 0

def is_odd(x):
    return x % 2 != 0

def describe_evenness(x):
    if is_even(x):
        print("It's even!")
    elif is_odd(x):
        print("It's odd!")
    else:
        print("It's neither even nor odd!")

def homework(x):
    for i in x:
        print(i ** 2)

my_first_list = [1, 'apple', 2, 'banana']
cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}

def homework(x):
    import pdb; pdb.set_trace()
    for i in x:
        print(i ** 2)

homework(cal_lookup)