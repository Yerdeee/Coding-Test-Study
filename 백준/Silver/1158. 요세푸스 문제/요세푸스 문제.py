from collections import deque

n, k = map(int, input().split())
q = deque(range(1, n+1))
result = []

while q:
    q.rotate(-(k-1))   # k-1만큼 왼쪽으로 회전
    result.append(q.popleft())  # k번째 사람 제거

print("<" + ", ".join(map(str, result)) + ">")
