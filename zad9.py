queue = []

while True:
    command = input()

    if command == "END":
        print(f"{len(queue)} people remaining.")
        break
    elif command == "PAID":
        while queue:
        
            print(queue.pop(0))
    else:
        queue.append(command)
                  