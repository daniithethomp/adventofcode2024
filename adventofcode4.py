import re

def part1():
    def left_to_right(lines):
        total_xmas = 0
        for line in lines:
            total_xmas += len(re.findall(r'XMAS',line))
            total_xmas += len(re.findall(r'SAMX',line))
        return total_xmas

    def top_to_bottom(lines):
        total_xmas = 0
        for i in range(len(lines[0])):
            total_xmas += len(re.findall(r'XMAS',''.join([line[i] for line in lines])))
            total_xmas += len(re.findall(r'SAMX',''.join([line[i] for line in lines])))
        return total_xmas

    def diagonal(lines):
        total_xmas = 0
        d = dict()
        for i in range(len(lines[0])):
            for j in range(len(lines)):
                d[i+j] = d.get(i+j,'') + lines[j][i]

        for key in d:
            print(d[key])
            total_xmas += len(re.findall(r'XMAS',d[key]))
            total_xmas += len(re.findall(r'SAMX',d[key]))

        d = dict()
        for i in range(len(lines[0])):
            for j in range(len(lines)):
                d[i-j] = d.get(i-j,'') + lines[j][i]

        for key in d:
            print(d[key])
            total_xmas += len(re.findall(r'XMAS',d[key]))
            total_xmas += len(re.findall(r'SAMX',d[key]))

        return total_xmas

    file = open("aoc4.txt", "r")
    lines = file.readlines()
    file.close()
    lines = [x.replace('\n','') for x in lines]

    total_xmas = 0
    total_xmas += left_to_right(lines) + top_to_bottom(lines) + diagonal(lines)
    print(total_xmas)

def part2():
    file = open("aoc4.txt", "r")
    lines = file.readlines()
    file.close()
    lines = [x.replace('\n','') for x in lines]

    total_xmas = 0
    for i in range(1,len(lines[0])-1):
        for j in range(1,len(lines)-1):
            if lines[j][i] == 'A':
                diag1 = ''.join([lines[j-1][i-1],lines[j][i],lines[j+1][i+1]])
                diag2 = ''.join([lines[j-1][i+1],lines[j][i],lines[j+1][i-1]])
                if len(re.findall(r'MAS|SAM',diag1)) > 0 and len(re.findall(r'MAS|SAM',diag2)) > 0:
                    total_xmas += 1
    print(total_xmas)

part1()
part2()