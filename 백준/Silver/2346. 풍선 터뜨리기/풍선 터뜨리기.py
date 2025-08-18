from collections import deque
q1 = deque()
q2 = deque()
result = []

n = int(input())

l = input().split()

for i in range(n):
    q1.append(int(l[i]))
    q2.append(int(i+1))
    
for _ in range (n):
    el = q1.popleft()
    re = q2.popleft()
    result.append(re)

    
    if el > 0:
        # 양수: 이미 하나 꺼냈으니 el-1칸만 왼쪽 회전
        q1.rotate(-(el - 1))
        q2.rotate(-(el - 1))
    else:
        # 음수: |el|칸 오른쪽 회전
        q1.rotate(-el)
        q2.rotate(-el)
        
print(' '.join(map(str, result)))