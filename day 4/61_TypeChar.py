import tkinter as tk

def show_text():
    teks = entry.get()
    output_label.config(text=teks)

def exit_app():
    window.destroy()

window = tk.Tk()
window.title("Pattern 28")

label_info = tk.Label(window, text="Your typed chars appear here:")
label_info.grid(row=0, column=0, padx=5, pady=5)

output_label = tk.Label(window, text="", width=15, anchor="w", relief="sunken")
output_label.grid(row=0, column=1, padx=5, pady=5)

entry = tk.Entry(window)
entry.grid(row=1, column=0, padx=5, pady=5)

btn_show = tk.Button(window, text="Show", command=show_text)
btn_show.grid(row=2, column=1, padx=5, pady=5)

btn_exit = tk.Button(window, text="Exit", command=exit_app)
btn_exit.grid(row=2, column=1, padx=5, pady=5)


window.columnconfigure(1, weight=1)

window.mainloop()