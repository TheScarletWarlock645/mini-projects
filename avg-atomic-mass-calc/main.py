print("\n*Average Atomic Mass Calculator*")
iso_num = int(input("\nHow many isotopes would you like to calculate: "))

calculations = {}
for i in range(0, iso_num):
    abundance = float(input(f"\nenter abundance(%) #{i + 1}: "))
    mass = float(input(f"enter mass #{i + 1}: "))

    key = f"calc_{i}"
    calculations[key] = (abundance / 100) * mass

    print()
    print(calculations[key])
    print()

atomic_mass = 0
for value in calculations.values():
    atomic_mass += float(value)

print(f"Average atomic mass: {atomic_mass}")
print(f"Average atomic mass (rounded): {round(atomic_mass, 2)}\n")
