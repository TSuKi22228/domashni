def hot_potato(players, n):
    queue = list(players)
    
    while len(queue) > 1:
        for _ in range(n - 1):
            queue.append(queue.pop(0))
        removed_player = queue.pop(0)
        print(f"Removed {removed_player}")

    print(f"Last is {queue[0]}")

players = input().split()
n = int(input())

hot_potato(players, n)