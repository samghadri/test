nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

num_list = list()

for num in nums:
    num_list.append(num)
print(num_list)

# list comprehension
my_comp_list = [item for item in nums]
print(my_comp_list)

my_squared_comp = [n * n for n in nums]
print(my_squared_comp)

# Even num
normal_for_loop_list = []
for num in nums:
    if num % 2 == 0:
        normal_for_loop_list.append(num)
print(normal_for_loop_list)

# list Comp Even num
list_comp_even = [item for item in nums if item % 2 == 0]
print(list_comp_even)

# lambda
my_list_lambda = filter(lambda n: n % 2 == 0, nums)
print(my_list_lambda)

# odd num
normal_for_loop_list_odd = []
for num in nums:
    if num % 2 == 1:
        normal_for_loop_list_odd.append(num)
print(normal_for_loop_list_odd)

# list Comprehension Odd number
list_com_odd = [num for num in nums if num % 2 == 1]
print(list_com_odd)

pair_list = []

for letter in 'abcd':
    for num in range(4):
        pair_list.append((letter, num))
print(pair_list)

# pair List Comprehension
pair_list_comp = [(letter, num) for letter in 'abcd' for num in range(4)]
print(pair_list_comp)

# Zip Create list of Tuples

name = ['Sam', 'Soheil', 'dawood', 'diego']
surnames = ['ghadri', 'ghaffari', 'zohrabeigi', 'abreu']
names_ziped = zip(name, surnames)
# print(dict(names_ziped))

# I want a dictionary{'name': 'surname:'} for each name put surname by zip builtin func zip(name, surname)
my_dict = {}
for first, second in names_ziped:
    # or you can remove names_ziped and specify the zip in for loop
    my_dict[first] = second
print(my_dict)

# Dic comprehension

dic_comp_zip = {first: family for first, family in zip(name, surnames)}
print(dic_comp_zip)

# set
nums_unset = [1, 1, 2, 3, 3, 2, 2, 3, 4, 4, 5, 5, 5, 6, 7, 8, 6, 5, 9, 9]
my_set = set()
for num in nums_unset:
    my_set.add(num)
print(my_set)

# dic set
my_dict_set = {n for n in nums_unset}
print(my_dict_set)



# generator Expresion
gen_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def gen_func(gen_list):
    for num in gen_list:
        yield num*num

my_gen = gen_func(gen_list)

print(next(my_gen))
print(next(my_gen))


lst = list()
for i in my_gen:
    lst.append(i)
print(lst)

# Gen ex

my_gen_ex = (num*num for num in gen_list)

for i in my_gen_ex:
    print(i)