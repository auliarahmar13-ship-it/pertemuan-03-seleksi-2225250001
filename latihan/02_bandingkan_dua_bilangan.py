
# Input: dua bilangan
# Proses: membandingkan nilainya
# Output: lebih besar, sama, atau lebih kecil

a = float(input("Bilangan pertama: "))
b = float(input("Bilangan kedua: "))

if a >= b:
    if a == b:
        print("Kedua bilangan sama.")
    else:
        print("Bilangan pertama lebih besar.")
else:
    print("Bilangan pertama lebih kecil.")