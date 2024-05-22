# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname, 'r')
except:
    print("Wrong file format")
    quit()
f_text = fh.read()
f_text_upper = f_text.upper()
fh.close()
print(f_text_upper.rstrip())

