angka_maksimal = 10

print(f"pemeriksaan angka 1 sampai {angka_maksimal}:")
print("-" * 30)

for i in range(1, angka_maksimal + 1):
    if i % 2 == 0:
        print(f"Angka {i} adalah GENAP")
    else:
        print(f"angka {i} adalah GANJIL")