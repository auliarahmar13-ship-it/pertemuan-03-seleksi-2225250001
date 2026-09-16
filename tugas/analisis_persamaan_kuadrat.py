
# Input: koefisien a, b, c
# Proses: menghitung diskriminan dan menentukan jenis akar
# Output: jenis akar persamaan kuadrat

print("Analisis Persamaan Kuadrat")

a = float(input("Koefisien a: "))
b = float(input("Koefisien b: "))
c = float(input("Koefisien c: "))

if a == 0:
    print("Bukan persamaan kuadrat.")
else:
    D = b ** 2 - 4 * a * c
    print(f"Diskriminan = {D:.2f}")

    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        print(f"Dua akar real: {x1:.2f} dan {x2:.2f}")

    elif D == 0:
        x = -b / (2 * a)
        print(f"Akar kembar: {x:.2f}")

    else:
        print("Tidak ada akar real.")