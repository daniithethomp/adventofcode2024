file = open("aoc1.txt", "r")
lines = file.readlines()
file.close()
lists = list(map(lambda x : x.split('   ',1), lines))
lists = [x for xs in lists for x in xs]
lists = [x.replace('\n','') for x in lists]
list1 = lists[0::2]
list2 = lists[1::2]
list1.sort()
list2.sort()

distance = sum(list(map(lambda x,y: abs(int(x) - (int(y))), list1, list2)))
print(f'Distance between two lists: {distance}')

similarity = 0
for i in list1:
    appearances = list2.count(i)
    similarity += appearances * int(i)

print(f'Similarity between two lists: {similarity}')
