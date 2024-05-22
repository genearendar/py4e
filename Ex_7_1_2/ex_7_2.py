fname = input("Enter file name: ")
try:
    file = open(fname)
except:
    print("File does not exist:", fname)
    quit()
count = 0
sum = 0
for line in file:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        sum= sum + float(line[19:].strip())
file.close()
avg = sum / count
print ("Average spam confidence:", avg)
