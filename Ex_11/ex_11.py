import re
file = open("regex_sum_2027784.txt")
numbers = re.findall("[0-9]+", file.read())
numbers = [int(number) for number in numbers]
print(sum(numbers))