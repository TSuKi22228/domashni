food_quantity = int(input())
orders = list(map(int, input().split()))

max_order = max(orders)


orders_complete = True


while orders:
    current_order = orders[0]
    if current_order <= food_quantity:
        food_quantity -= current_order
        orders.pop(0)
    else:
        orders_complete = False
        break


print(max_order)


if orders_complete:
    print("Orders complete")
else:
    remaining_orders = ', '.join(map(str, orders))
    print(f"Remaining order: {remaining_orders}")