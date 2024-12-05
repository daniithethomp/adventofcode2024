import re

file = open("aoc3.txt", "r")
lines = file.readlines()
file.close()
lines = [x.replace('\n','') for x in lines]
operations = list(map(lambda x: re.findall(r'mul\(\d\d?\d?,\d\d?\d?\)|don?\'?t?\(\)',x),lines))
operations = [x for xs in operations for x in xs]
print(operations)
res = 0
do = True
for operation in operations:
    print(operation)
    if operation == 'don\'t()':
        do = False
    elif operation == 'do()':
        do = True
    elif do:
        nums = re.findall(r'\d\d?\d?',operation)
        res += int(nums[0]) * int(nums[1])

print(res)