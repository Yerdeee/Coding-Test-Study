# n = int(input())
# result = []
#stack = list(map(int, input().split()))

  
# for i in range(n) :
#    num = stack.pop()
#    if len(stack) == 0 :
#        result.append(0)
#        break
    
#    else :
#        idx = len(stack)-1

#        while idx >= 0 and stack[idx]<num :
#            idx -= 1
#        result.append(idx+1)

# result.reverse()
# print(' '.join(map(str, result)))

n = int(input())
heights = list(map(int, input().split()))
stack = []  # (인덱스, 높이)
result = [0] * n

for i in range(n):
    while stack and stack[-1][1] < heights[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1][0] + 1  # 인덱스는 0부터 시작하니까 +1
    stack.append((i, heights[i]))

print(' '.join(map(str, result)))

