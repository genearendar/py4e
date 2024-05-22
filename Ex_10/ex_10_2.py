#open the file
file = open("mbox-short.txt")
hour_count = dict()

#build the dictionary of hours and their counts
for line in file:
    if line.startswith("From:"):
        continue
    elif line.startswith("From"):
        line_parts = line.split()
        time = line_parts[len(line_parts) - 2]
        hour = time.split(":")[0]
        hour_count[hour] = hour_count.get(hour, 0) + 1

for hour, count in sorted(hour_count.items()):
    print(hour, count)
file.close()






# Find the most popular address
# big_count = None
# big_email = None
# for key,value in mail_count.items():
#     if big_email is None:
#         big_email = key
#         big_count = value
#     elif big_count < value:
#         big_email = key
#         big_count = value
# print(big_email, big_count)
# file.close()
