import sys
input = sys.stdin.readline

quest = input()
parts = quest.split('-')
res = sum(map(int, parts[0].split('+')))

for part in parts[1:]:
    res -= sum(map(int,part.split('+')))

print(res)