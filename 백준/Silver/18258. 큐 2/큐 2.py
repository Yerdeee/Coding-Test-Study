import sys
input = sys.stdin.readline


command = int(input()) # 명령의 수
que = []
pointer = 0

for i in range (command):
    com = input().split() # 띄어쓰기 기준으로 분리
    
    if com[0] == 'push': # push 명령 구현
        que.append(int(com[1]))
        
    elif com[0] == 'pop': # pop 명령 구현
        if len(que) == pointer :
            print(-1)
        else :
            print(que[pointer])
            pointer += 1
            
    elif com[0] == 'size': # size 명령 구현
        print(len(que) - pointer)
        
    elif com[0] == 'empty':
        if len(que) == pointer :
            print(1)
        else :
            print(0)
            
    elif com[0] == 'front' :
        if len(que) == pointer :
            print(-1)
        else :
            print(que[pointer])
            
    elif com[0] == 'back' : 
        if len(que) == pointer :
            print(-1)
        else :
            print(que[-1])
        
    