import os
import zipfile
import py7zr
import patoolib
import tkinter as tk
from tkinter import filedialog, messagebox
import shutil

def extract_archive(archive_path, dest_path):
    try:
        if archive_path.endswith('.zip'):
            with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                zip_ref.extractall(dest_path)
        elif archive_path.endswith('.7z'):
            with py7zr.SevenZipFile(archive_path, mode='r') as z:
                z.extractall(path=dest_path)
        elif archive_path.endswith('.rar'):
            patoolib.extract_archive(archive_path, outdir=dest_path)
        else:
            messagebox.showerror("Erreur", "Format de fichier non supporté.")
            return
        messagebox.showinfo("Succès", "L'extraction est terminée avec succès!")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

def select_archive_file():
    archive_path = filedialog.askopenfilename(filetypes=[("Tous les fichiers d'archive", "*.zip *.7z *.rar"), 
                                                         ("Fichiers ZIP", "*.zip"), 
                                                         ("Fichiers 7z", "*.7z"), 
                                                         ("Fichiers RAR", "*.rar")])
    archive_entry.delete(0, tk.END)
    archive_entry.insert(0, archive_path)

def select_destination_folder():
    dest_path = filedialog.askdirectory()
    dest_entry.delete(0, tk.END)
    dest_entry.insert(0, dest_path)

def on_extract_click():
    archive_path = archive_entry.get()
    dest_path = dest_entry.get()

    if archive_path and dest_path:
        extract_archive(archive_path, dest_path)
    else:
        messagebox.showwarning("Attention", "Veuillez sélectionner un fichier d'archive et un dossier de destination.")

# Interface graphique avec Tkinter
root = tk.Tk()
root.title("Extracteur d'Archives")

# Sélection du fichier d'archive
tk.Label(root, text="Fichier d'archive:").grid(row=0, column=0, padx=10, pady=10)
archive_entry = tk.Entry(root, width=50)
archive_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Parcourir...", command=select_archive_file).grid(row=0, column=2, padx=10, pady=10)

# Sélection du dossier de destination
tk.Label(root, text="Dossier de destination:").grid(row=1, column=0, padx=10, pady=10)
dest_entry = tk.Entry(root, width=50)
dest_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Parcourir...", command=select_destination_folder).grid(row=1, column=2, padx=10, pady=10)

# Bouton d'extraction
tk.Button(root, text="EXTRAIRE TOUT", command=on_extract_click, bg="green", fg="white").grid(row=2, column=1, pady=20)

root.mainloop()
