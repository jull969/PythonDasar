a = float(input("\nMasukkan sisi atas trapesium: "))
b = float(input("Masukkan sisi bawah trapesium: "))
c = float(input("Masukkan sisi miring kiri trapesium: "))
d = float(input("Masukkan sisi miring kanan trapesium: "))
t = float(input("Masukkan tinggi trapesium: "))

keliling_trapesium = a + b + c + d
luas_trapesium = 0.5 * (a + b) * t

print("\n--- TRAPESIUM ---")
print("Keliling =", keliling_trapesium)
print("Luas =", luas_trapesium)