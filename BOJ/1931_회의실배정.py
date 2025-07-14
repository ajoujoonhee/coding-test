import sys
input = sys.stdin.readline

N = int(input())
res = 0
meeting = [list(map(int, input().split())) for _ in range(N)]

# 끝나는 시간이 이른 순서로 sort
meeting.sort(key = lambda x: (x[1], x[0]))

s,e = 0,0 # 시작 변수 s, 끝 변수 e

# 기존 e의 값이 새로 들어오는 s의 값보다 작거나 같아야 회의실 배정이 가능
for i in range(N):
    if e <= meeting[i][0]:
        res += 1
        s = meeting[i][0]
        e = meeting[i][1]

print(res)
