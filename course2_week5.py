name = input('Please Enter the input')
if len(name) < 1:
    name = 'mbox-short.txt'
handle = open(name)

count = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    time = words[5]
    part_time = time.split(':')
    hour = part_time[0]
    count[hour] = count.get(hour,0)+1

for key,value in sorted(count.items()):
    print(key,value)