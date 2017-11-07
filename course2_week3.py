fname = input("Enter file name: ")
fh = open(fname)
lst = []
for line in fh:
    line = line.rstrip()
    for i in line.split():
        if not i in lst:
            lst.append(i)
lst.sort()
print(list(lst))