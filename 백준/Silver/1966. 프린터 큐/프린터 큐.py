import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    q = deque([(priorities[i], i) for i in range(n)])  # (중요도, 인덱스)
                
    count = 0
    while q:
        cur = q.popleft()
        # 현재 문서보다 중요도가 높은 문서가 하나라도 있으면 뒤로 보냄
        if any(cur[0] < other[0] for other in q):
            q.append(cur)
        else:
            count += 1  # 출력
            if cur[1] == m:  # 찾는 문서라면
                print(count)
                break
    