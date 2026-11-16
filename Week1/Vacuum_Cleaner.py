roomA = input("Enter status of A (Clean/Dirty): ")
roomB = input("Enter status of B (Clean/Dirty): ")
vac_pos = input("Enter position of Vacuum (A/B): ")
for i in range(4):
    print("\nRoom A status:", roomA)
    print("Room B status:", roomB)
    print("Vacuum position:", vac_pos)
    if vac_pos == "A":
        if roomA == "Dirty":
            print("Action = Suck")
            roomA = "Clean"
        else:
            print("Action = Move")
            vac_pos = "B"
    elif vac_pos == "B":
        if roomB == "Dirty":
            print("Action = Suck")
            roomB = "Clean"
        else:
            print("Action = Move")
            vac_pos = "A"