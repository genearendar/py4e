file = open("mbox-short.txt")
mail_count = dict()
for line in file:
    if line.startswith("From:"):
        continue
    elif line.startswith("From"):
        email = line.split()[1]
        mail_count[email] = mail_count.get(email, 0) + 1
big_count = None
big_email = None
for key,value in mail_count.items():
    if big_email is None:
        big_email = key
        big_count = value
    elif big_count < value:
        big_email = key
        big_count = value
print(big_email, big_count)
file.close()
