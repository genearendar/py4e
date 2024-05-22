file = open("mbox-short.txt")
count = 0
for line in file:
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        count = count + 1
        print(line.split()[1])
print("There were", count, "lines in the file with From as the first word")
