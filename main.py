import tkinter as tk
from tkinter import filedialog
from kd_player import KDPlayer, kd_info

player = KDPlayer()

def betoltes():
    path = filedialog.askopenfilename(filetypes=[("MP3 fájlok", "*.mp3")])
    if path:
        player.load(path)
        status_label.config(text="Betöltve: " + path.split("/")[-1])

def inditas():
    player.play()
    status_label.config(text="Lejátszás...")

def pauza():
    player.pause()
    status_label.config(text="Szünetelve")

def folytat():
    player.unpause()
    status_label.config(text="Folytatás")

def stop():
    player.stop()
    status_label.config(text="Leállítva")

root = tk.Tk()
root.title("KD Mini Zenelejátszó")

status_label = tk.Label(root, text="Válassz zenét...", font=("Arial", 12))
status_label.pack(pady=10)

tk.Button(root, text="🎵 Fájl betöltése", command=betoltes, width=20).pack(pady=4)
tk.Button(root, text="▶ Lejátszás", command=inditas, width=20).pack(pady=4)
tk.Button(root, text="⏸ Szünet", command=pauza, width=20).pack(pady=4)
tk.Button(root, text="⏵ Folytatás", command=folytat, width=20).pack(pady=4)
tk.Button(root, text="⏹ Stop", command=stop, width=20).pack(pady=4)

tk.Label(root, text=kd_info(), fg="grey").pack(pady=10)

root.mainloop()
