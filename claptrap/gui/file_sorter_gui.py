# gui/file_sorter_gui.py
# ------------------------------------------------------------
# GUI-Komponenten zum Sortieren von Dateien
# ------------------------------------------------------------
import tkinter as tk
from tkinter import filedialog, messagebox
from claptrap.core.file_sorter import sort_files

def create_file_sorter_frame(root, rules):
    """
    Erstellt den Frame für Quell-/Zielordner, Kategorie und Sortierbutton.
    Gibt Frame zurück (wird im Hauptfenster gepackt).
    """
    frame = tk.Frame(root)
    
    # Variablen
    source_var = tk.StringVar()
    target_var = tk.StringVar()
    category_var = tk.StringVar(value="EÜR")

    # Quellordner
    tk.Label(frame, text="Quellordner:", bg="#2B2B2B", fg="white").grid(row=0, column=0, sticky="w")
    tk.Entry(frame, textvariable=source_var, width=50).grid(row=0, column=1)
    tk.Button(frame, text="Auswählen", command=lambda: select_folder(source_var)).grid(row=0, column=2)
    
    # Zielordner
    tk.Label(frame, text="Zielordner:").grid(row=1, column=0, sticky="w")
    tk.Entry(frame, textvariable=target_var, width=50).grid(row=1, column=1)
    tk.Button(frame, text="Auswählen", bg="#4CAF50", fg="white", command=lambda: select_folder(target_var)).grid(row=1, column=2)

    # Kategorie
    tk.Label(frame, text="Kategorie:").grid(row=2, column=0, sticky="w")
    tk.OptionMenu(frame, category_var, "EÜR", "Privat").grid(row=2, column=1, sticky="w")

    # Sortierbutton
    sort_button = tk.Button(frame, text="Dateien sortieren",
                        bg="#4CAF50", fg="white",
                        activebackground="#45A049",  # beim Klicken
                        highlightbackground="#4CAF50",  # Hintergrund initial sichtbar
                        command=lambda: sort_button_click(source_var, target_var, category_var, rules))
    sort_button.grid(row=3, column=1, pady=10)


    return frame

# --------------------------
# Hilfsfunktionen

def select_folder(var):
    folder = filedialog.askdirectory()
    if folder:
        var.set(folder)

def sort_button_click(source_var, target_var, category_var, rules):
    source_folder = source_var.get()
    target_folder = target_var.get()
    category = category_var.get()
    if not source_folder or not target_folder:
        messagebox.showwarning("Fehler", "Bitte Quell- und Zielordner auswählen.")
        return
    moved_files = sort_files(source_folder, target_folder, category, rules)
    messagebox.showinfo("Fertig", f"{moved_files} Dateien verschoben.")
