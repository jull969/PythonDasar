import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import math

BIAYA_PER_JAM = 2000

def hitung_biaya():
    try:
        no_plat = entry_plat.get()
        masuk = entry_masuk.get()
        keluar = entry_keluar.get()

        if not no_plat:
            messagebox.showwarning("Peringatan", "No Plat harus diisi!")
            return

        # Format waktu HH:MM
        jam_masuk = datetime.strptime(masuk, "%H:%M")
        jam_keluar = datetime.strptime(keluar, "%H:%M")

        selisih = (jam_keluar - jam_masuk).seconds / 3600
        lama_jam = math.ceil(selisih)  # dibulatkan ke atas
        biaya = lama_jam * BIAYA_PER_JAM

        entry_biaya.delete(0, tk.END)
        entry_biaya.insert(0, str(biaya))

        # Tambahkan ke tabel
        tree.insert("", "end", values=(no_plat, masuk, keluar, biaya))

        # Kosongkan input
        entry_plat.delete(0, tk.END)
        entry_masuk.delete(0, tk.END)
        entry_keluar.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Format waktu harus HH:MM")

# ================= GUI =================
root = tk.Tk()
root.title("Aplikasi Parkir Kelompok 6")
root.geometry("800x500")

# Frame kiri (input)
frame_input = tk.Frame(root)
frame_input.pack(side=tk.LEFT, padx=20, pady=20)

tk.Label(frame_input, text="No Plat Polisi").grid(row=0, column=0, sticky="w")
entry_plat = tk.Entry(frame_input)
entry_plat.grid(row=0, column=1)

tk.Label(frame_input, text="Waktu Masuk (HH:MM)").grid(row=1, column=0, sticky="w")
entry_masuk = tk.Entry(frame_input)
entry_masuk.grid(row=1, column=1)

tk.Label(frame_input, text="Waktu Keluar (HH:MM)").grid(row=2, column=0, sticky="w")
entry_keluar = tk.Entry(frame_input)
entry_keluar.grid(row=2, column=1)

tk.Label(frame_input, text="Biaya").grid(row=3, column=0, sticky="w")
entry_biaya = tk.Entry(frame_input)
entry_biaya.grid(row=3, column=1)

tk.Button(frame_input, text="Hitung", command=hitung_biaya).grid(row=4, columnspan=2, pady=10)

# Label biaya besar
frame_kanan = tk.Frame(root)
frame_kanan.pack(side=tk.RIGHT, padx=20)

tk.Label(frame_kanan, text="Biaya Per Jam", fg="red", font=("Arial", 16)).pack()
tk.Label(frame_kanan, text="Rp. 2.000", fg="red", font=("Arial", 28, "bold")).pack()

# Tabel
columns = ("No Plat", "Masuk", "Keluar", "Biaya")
tree = ttk.Treeview(root, columns=columns, show="headings", height=8)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(pady=20)

root.mainloop()