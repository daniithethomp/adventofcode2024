import itertools

def isSafe(x):
    combinations = list(itertools.combinations(x,len(x)-1))
    safe_comb = False
    for comb in combinations:
        decreasing = True
        increasing = True
        distances_between_1_and_3 = True
        for i in range(0,len(comb)-1):
            num1 = int(comb[i])
            num2 = int(comb[i+1])
            if num1 > num2:
                increasing = False
            elif num1 < num2:
                decreasing = False
            else:
                increasing = False
                decreasing = False
            if abs(num1 - num2) > 3 or abs(num1 - num2) < 1:
                distances_between_1_and_3 = False
        if (increasing or decreasing) and distances_between_1_and_3:
            safe_comb = True
            break
    return safe_comb
        


file = open("aoc2.txt", "r")
lines = file.readlines()
lines = [x.replace('\n','') for x in lines]
file.close()

safe = 0
nums = list(map(lambda x : x.split(' '), lines))
safe_reports = list(filter(isSafe,nums))
print(f"Number of safe reports: {len(safe_reports)}")