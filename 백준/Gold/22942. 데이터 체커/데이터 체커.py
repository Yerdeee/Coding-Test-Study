#    n = int(input())
#    lst = []
#    x = []
#
#    for i in range(n):
#        a, b = map(int, input().split())
#        lst.append((a-b, a+b))
#        x.append(a)
#        x.append(b)
#
#    if len(lst) != len(set(lst)) : # 중복 확인
#        print('NO')
#        exit(0)
#    elif len(x) != len(set(x)) :
#        print('NO')
#        exit(0)
#
#    lst.sort()
#    for i1 in lst :
#        for i2 in lst :
#            if i2[0] > i1[0] and i2[0] < i1[1]:
#                if i2[1] > i1[1] :
#                    print('NO')
#                    exit(0)
#
#    print('YES')
            
import sys 
n = int(sys.stdin.readline())
circles = []

for _ in range(n):
    x, r = map(int, sys.stdin.readline().split())
    l, rr = x - r, x + r
    circles.append((l, rr))

# 왼쪽 기준 정렬
circles.sort()

stack = []
for l, r in circles:
    while stack and stack[-1][1] < l:
        stack.pop()
    if stack and stack[-1][1] >= l and stack[-1][1] <= r:
        print("NO")
        exit(0)
    stack.append((l, r))

print("YES")




