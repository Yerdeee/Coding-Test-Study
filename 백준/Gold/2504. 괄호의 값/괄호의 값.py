bat = list(input())
stack = []    
n = 0   
    
for i in bat :
    if stack and stack[-1] == '(' and i == ')' : # 2 만들기
        stack.pop()
        stack.append(2)
        
    elif stack and stack[-1] == '[' and i == ']': # 3 만들기
        stack.pop()
        stack.append(3)
    
    elif i == ')' :
        n = 0
        while stack and isinstance(stack[-1], int):
            n += stack.pop()
        if not stack or stack[-1] != '(' :
            print(0)
            exit(0)
        stack.pop()
        stack.append(2*(n if n else 1))
        
    
    elif i == ']' :
        n = 0
        while stack and isinstance(stack[-1], int):
            n += stack.pop()
        if not stack or stack[-1] != '[':
            print(0)
            exit(0)
        stack.pop()
        stack.append(3 * (n if n else 1))
    
    else :
        stack.append(i)
    
# 마지막 검증
if all(isinstance(x, int) for x in stack):
    print(sum(stack))
else:
    print(0)


    