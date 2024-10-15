fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    print(line.strip().upper())
