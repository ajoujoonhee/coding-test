#백준 10828번: 스택
import sys
input = sys.stdin.readline

N = int(input())
stk = []

for i in range(N):
    cmd = input().strip().split()
    if cmd[0] == 'push':
        x = int(cmd[1])
        stk.append(x)
    elif cmd[0] == 'pop':
        if stk:
            print(stk.pop())
        else: print(-1)
    elif cmd[0] == 'size':
        print(len(stk))
    elif cmd[0] == 'empty':
        if len(stk) == 0:
            print(1)
        else: print(0)
    elif cmd[0] == 'top':
        if stk: print(stk[-1])
        else: print(-1)
        