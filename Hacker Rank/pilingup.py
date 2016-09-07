from collections import deque
T = input()
finish = [i for i in range(T)]
for each in range(T):
    N = input()
    d = deque(map(int, raw_input().strip().split()))

    side = 0
    

    for i in range(N):
        if d[0] >= d[-1]:
            if side == 0:
                side = d.popleft()
                finish[each] = 'Yes'
            elif d[0] <= side:
                side = d.popleft()
                finish[each] = 'Yes'
            else:
                finish[each] = 'No'
        elif d[-1] > d[0]:
            if side == 0:
                side = d.pop()
                finish[each] = 'Yes'
            elif d[-1] <= side:
                side = d.pop()
                finish[each] = 'Yes'
            else:
                finish[each] = 'No'

for each in finish:
    print each