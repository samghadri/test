fname = input("Enter file name: ")
fh = open(fname)

for char in fh:
    char = char.rstrip()
    print(char.upper())
