counts = dict()
bigkey = None
bigvalue = None
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

for line in handle:
    if line.startswith('From:'):
        word = line.split()
        email = word[1]
        counts[email] = counts.get(email, 0)+1

        for k,v in counts.items():
            if bigvalue is None or v > bigvalue:
                bigkey = k
                bigvalue = v
print(bigkey,bigvalue)
