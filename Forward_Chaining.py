KB = [
    "American(Robert)",
    "Missile(T1)",
    "Owns(A,T1)",
    "Enemy(A,America)"
]

print("Initial Knowledge Base:")
for fact in KB:
    print(fact)
new_fact = True

while new_fact:
    new_fact = False
    if "Missile(T1)" in KB and "Weapon(T1)" not in KB:
        KB.append("Weapon(T1)")
        print("\nInferred: Weapon(T1)")
        print("Derived from: Missile(T1)")
        new_fact = True
    if ("Missile(T1)" in KB and "Owns(A,T1)" in KB
            and "Sells(Robert,T1,A)" not in KB):

        KB.append("Sells(Robert,T1,A)")
        print("\nInferred: Sells(Robert,T1,A)")
        print("Derived from: Missile(T1) AND Owns(A,T1)")
        new_fact = True
    if ("Enemy(A,America)" in KB and "Hostile(A)" not in KB):

        KB.append("Hostile(A)")
        print("\nInferred: Hostile(A)")
        print("Derived from: Enemy(A,America)")
        new_fact = True
    if ("American(Robert)" in KB
            and "Weapon(T1)" in KB
            and "Sells(Robert,T1,A)" in KB
            and "Hostile(A)" in KB
            and "Criminal(Robert)" not in KB):

        KB.append("Criminal(Robert)")
        print("\nInferred: Criminal(Robert)")
        print("Derived from:")
        print("American(Robert)")
        print("Weapon(T1)")
        print("Sells(Robert,T1,A)")
        print("Hostile(A)")

        new_fact = True
print("\nFinal Knowledge Base:")
for fact in KB:
    print(fact)

if "Criminal(Robert)" in KB:
    print("\nGoal Proved: Robert is Criminal")
else:
    print("\nGoal Not Proved")