import sys

input = sys.stdin.readline

n = int(input().strip())
expr = input().strip()               # 후위 표기식
vals = [float(input().strip()) for _ in range(n)]  # A, B, ... 에 대응하는 값

stack = []
for ch in expr:
    if 'A' <= ch <= 'Z':             # 피연산자(변수)
        stack.append(vals[ord(ch) - ord('A')])
    else:                            # 연산자
        b = stack.pop()
        a = stack.pop()
        if ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)
        elif ch == '*':
            stack.append(a * b)
        elif ch == '/':
            stack.append(a / b)

print(f"{stack[-1]:.2f}")
