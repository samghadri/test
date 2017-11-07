fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(':')
    num = float(line[pos+1:])
    total = total +num
    count = count + 1
print ('Average spam confidence:', total/count)