import math

jari_jari = float(input("Masukkan jari-jari tabung: "))
tinggi_tabung = float(input("Masukkan tinggi tabung: "))

volume_tabung = math.pi * jari_jari * jari_jari * tinggi_tabung

print("\n--- TABUNG ---")
print("Volume =", volume_tabung)