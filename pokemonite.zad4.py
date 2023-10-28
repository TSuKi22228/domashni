clothes = list(map(int, input().split()))
shelf_capacity = int(input())

shelves_used = 0
current_shelf_capacity = shelf_capacity

for cloth in clothes:
    if cloth <= current_shelf_capacity:
        current_shelf_capacity -= cloth
    else:
        shelves_used += 1
        current_shelf_capacity = shelf_capacity - cloth
if current_shelf_capacity < shelf_capacity:
    shelves_used += 1

print(shelves_used)