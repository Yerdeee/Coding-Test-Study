bat = list(input())
stack = []
cnt = 0


for i in range(len(bat)) :
    if bat[i] == '(' :
        stack.append(bat[i])
    if bat[i] == ')' and bat[i-1] == '(' :
        stack.pop()
        cnt += len(stack)
    elif bat[i] == ')' and bat[i-1] == ')' :
        stack.pop()
        cnt += 1
    
print(cnt)
