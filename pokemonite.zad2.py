n = int(input())
stack = []

max_num = float('-inf')
min_num = float('inf')

for _ in range(n):
    command = input().split()
    operation = int(command[0])

    if operation == 1:
        number = int(command[1])
        stack.append(number)
        max_num = max(max_num, number)
        min_num = min(min_num, number)
    elif operation == 2:
        if stack:
            popped = stack.pop()
            if popped == max_num:
                max_num = max(stack) if stack else float('-inf')
            if popped == min_num:
                min_num = min(stack) if stack else float('inf')
    elif operation == 3:
        print(max_num)
    elif operation == 4:
        print(min_num)
    elif operation == 5:
        print(len(stack))

while stack:
    print(stack.pop())