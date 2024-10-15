__author__ = "Prayas"

fname = input("Enter file name: ")

try:
    fhandle = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

count = 0
total = 0

for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    pos = line.find(':')
    value = float(line[pos+1:].strip())
    
    total += value
    count += 1

if count > 0:
    average = total / count
    print("Average spam confidence:", average)
else:
    print("No relevant lines found.")