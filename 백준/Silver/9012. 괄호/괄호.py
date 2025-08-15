n = int(input())

for _ in range (n) :
    ps = input()
    l = []
    valid = True
    
    for i in range (len(ps)):
        if ps[i] == '(':
            l.append(0)
        else: 
            if not l:
                valid = False
                break
            l.pop()
            
    if valid and not l:
        print("YES")
    else:
        print("NO")
        
    