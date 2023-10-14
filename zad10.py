def party_host():
    bites = int(input())
    guest = []

    while True:
        command = input()

        if command == "START":
            break

        guest.append(command)
    while True:
        command = input()
        
        if command == "End":
            break
        
        tokens = command.split()
        
        if tokens[0] == "refill":
            bites += int(tokens[1])
        else:
            person_name = guest.pop(0)
            bites_needed = int(tokens[0])
            
            if bites >= bites_needed:
                print(f"{person_name} take bites")
                bites -= bites_needed
            else:
                print(f"{person_name} must wait")
    
    print(f"{bites} bites left")

party_host()