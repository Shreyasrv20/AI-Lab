roomA = input("Enter status of Room A (Clean/Dirty): ")
roomB = input("Enter status of Room B (Clean/Dirty): ")
vac_pos = input("Enter vacuum position (A/B): ")
while roomA == "Dirty" or roomB == "Dirty":
    print("\nRoom A:", roomA)
    print("Room B:", roomB)
    print("Vacuum Position:", vac_pos)
    if vac_pos == "A":
        if roomA == "Dirty":
            print("Action = Suck")
            roomA = "Clean"
        else:
            print("Action = Move to B")
            vac_pos = "B"
    elif vac_pos == "B":
        if roomB == "Dirty":
            print("Action = Suck")
            roomB = "Clean"
        else:
            print("Action = Move to A")
            vac_pos = "A"
print("\nRoom A:", roomA)
print("Room B:", roomB)
print("Goal Achieved! Both rooms are clean.")