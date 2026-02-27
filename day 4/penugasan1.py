import tkinter as tk
from tkinter import messagebox

def hitung_total():
    try:
        harga = float(entry_harga.get())
        kuantitas = int(entry_kuantitas.get())
        total = harga * kuantitas
        label_total.config(text=f"Total: Rp. {total:,.2f}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# Membuat window
root = tk.Tk()
root.title("Program Kasir")
root.geometry("300x250")

# Label Harga
label_harga = tk.Label(root, text="Harga:")
label_harga.pack(pady=5)

entry_harga = tk.Entry(root)
entry_harga.pack(pady=5)

# Label Kuantitas
label_kuantitas = tk.Label(root, text="Kuantitas:")
label_kuantitas.pack(pady=5)

entry_kuantitas = tk.Entry(root)
entry_kuantitas.pack(pady=5)

# Tombol Hitung
btn_hitung = tk.Button(root, text="Hitung Total", command=hitung_total)
btn_hitung.pack(pady=10)

# Label Total
label_total = tk.Label(root, text="Total: Rp. 0.00")
label_total.pack(pady=5)

root.mainloop()