# https://favtutor.com/blogs/valid-parentheses
parentheses = input()
stack = []
opening = set('([{')
closing = set(')]}')
pair = {')': '(', ']': '[', '}': '{'}
valid = True
for i in parentheses:
    if i in opening:
        stack.append(i)
    if i in closing:
        if not stack:
            valid = False
        elif stack.pop() != pair[i]:
            valid = False
        else:
            continue
if valid:
    print("YES")
else:
    print("NO")
