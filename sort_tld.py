li = [2, 1, 3, 7, 6, 4, 8, 5, 9]

s_li = sorted(li, reverse=True)
print('the sorted listed list is: \t %s' % s_li)

tup = (-1, -3, -2, 4, 3, 1, 6, 7, 5, 9, 8, 2)
s_tup = sorted(tup)

print(s_tup)

di = {'name': 'Sam', 'Job': 'programmer', 'age': None, 'os': 'Mac'}
s_di = sorted(di)

for k, v in di.items():
    print([k, v])

ls_t = [-5, -6, -7, 4, 3, 1, 2]
s_tup = sorted(ls_t, key=abs)

print(s_tup)


class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    def __repr__(self):
        return '{} {} {}'.format(self.name, self.age, self.pay)


e1 = Employee('John', 22, 50000)
e2 = Employee('Tim', 28, 60000)
e3 = Employee('Sam', 28, 70000)

employees = [e1, e2, e3]


def e_sort(emp):
    return emp.pay


sorted_employees = sorted(employees, key=e_sort, reverse=True)

print(sorted_employees)
