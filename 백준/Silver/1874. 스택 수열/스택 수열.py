n = int(input())
stack = []
num = 1
status = '+'
result = []

for i in range(n):
    target = int(input())
    
    while num <= target :
        stack.append(num)
        result.append('+')
        num += 1

    if stack[-1] == target :
        stack.pop()
        result.append('-')
    else :
        print('NO')
        exit(0)
            

            

for i in result :
    print(i)
        