# ------------------------------------------------------------
# Claptrap 0.1 – Dokumentensortierer mit Kategorie-Auswahl
# Version: 0.1
# 
# Features:
# - Dateien nach Schlüsselwort in Unterordner verschieben
# - Regeln mit Kategorie (EÜR / Privat)
# - Kategorie-Auswahl beim Sortieren
# - Regeln direkt im GUI verwalten (hinzufügen, bearbeiten, löschen)
# - Regeln werden in rules.json gespeichert
# ------------------------------------------------------------

import os
import shutil
import json
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# --------------------------
# Datei, in der die Regeln gespeichert werden
RULES_FILE = "rules.json"

# --------------------------
# Regeln laden oder Standard erstellen
if os.path.exists(RULES_FILE):
    with open(RULES_FILE, "r", encoding="utf-8") as f:
        rules = json.load(f)
else:
    # Standard-Regeln: key -> {folder, category}
    rules = {
        "rechnung": {"folder": "Rechnungen", "category": "EÜR"},
        "beleg": {"folder": "Belege", "category": "EÜR"},
        "kontoauszug": {"folder": "Kontoauszüge", "category": "EÜR"},
        "steuer": {"folder": "Steuerunterlagen", "category": "EÜR"},
        "gehalt": {"folder": "Gehalt", "category": "Privat"},
        "versicherung": {"folder": "Versicherungen", "category": "Privat"},
        "vertrag": {"folder": "Verträge", "category": "Privat"},
    }

# --------------------------
# Funktionen zur Regelverwaltung

def save_rules():
    """Speichert die Regeln in rules.json und aktualisiert die GUI-Liste"""
    with open(RULES_FILE, "w", encoding="utf-8") as f:
        json.dump(rules, f, indent=4, ensure_ascii=False)
    update_rule_list()

def add_rule():
    """Neue Regel mit Kategorie hinzufügen"""
    keyword = simpledialog.askstring("Neue Regel", "Schlüsselwort:")
    if not keyword:
        return
    folder = simpledialog.askstring("Neue Regel", "Zielordner (Unterordner):")
    if not folder:
        return
    category = simpledialog.askstring("Neue Regel", "Kategorie (EÜR oder Privat):", initialvalue="EÜR")
    if category not in ["EÜR", "Privat"]:
        messagebox.showwarning("Kategorie", "Kategorie muss 'EÜR' oder 'Privat' sein.")
        return
    rules[keyword.lower()] = {"folder": folder, "category": category}
    save_rules()

def edit_rule():
    """Existierende Regel bearbeiten"""
    selected = rule_list.curselection()
    if not selected:
        messagebox.showwarning("Bearbeiten", "Bitte eine Regel auswählen")
        return
    keyword = rule_list.get(selected[0]).split(" → ")[0]
    rule = rules[keyword]
    new_keyword = simpledialog.askstring("Bearbeiten", "Neues Schlüsselwort:", initialvalue=keyword)
    if not new_keyword:
        return
    new_folder = simpledialog.askstring("Bearbeiten", "Neuer Zielordner:", initialvalue=rule["folder"])
    if not new_folder:
        return
    new_category = simpledialog.askstring("Bearbeiten", "Kategorie (EÜR oder Privat):", initialvalue=rule["category"])
    if new_category not in ["EÜR", "Privat"]:
        messagebox.showwarning("Kategorie", "Kategorie muss 'EÜR' oder 'Privat' sein.")
        return
    del rules[keyword]
    rules[new_keyword.lower()] = {"folder": new_folder, "category": new_category}
    save_rules()

def delete_rule():
    """Ausgewählte Regel löschen"""
    selected = rule_list.curselection()
    if not selected:
        messagebox.showwarning("Löschen", "Bitte eine Regel auswählen")
        return
    keyword = rule_list.get(selected[0]).split(" → ")[0]
    if messagebox.askyesno("Löschen", f"Regel '{keyword}' wirklich löschen?"):
        del rules[keyword]
        save_rules()

def update_rule_list():
    """Listbox in GUI aktualisieren"""
    rule_list.delete(0, tk.END)
    for k, v in rules.items():
        rule_list.insert(tk.END, f"{k} → {v['folder']} ({v['category']})")

# --------------------------
# Ordner auswählen

def select_source_folder():
    folder = filedialog.askdirectory(title="Quellordner auswählen")
    if folder:
        source_var.set(folder)

def select_target_folder():
    folder = filedialog.askdirectory(title="Zielordner auswählen")
    if folder:
        target_var.set(folder)

# --------------------------
# Dateien sortieren

def sort_files():
    """Dateien basierend auf Kategorie und Regeln verschieben"""
    source_folder = source_var.get()
    target_folder = target_var.get()
    category = category_var.get()
    if not source_folder or not target_folder:
        messagebox.showwarning("Fehler", "Bitte Quell- und Zielordner auswählen.")
        return
    moved_files = 0
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path):
            file_lower = file.lower()
            for keyword, rule in rules.items():
                if rule["category"] != category:
                    continue  # nur Regeln der gewählten Kategorie
                if keyword in file_lower:
                    dest_folder = os.path.join(target_folder, rule["folder"])
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    moved_files += 1
                    break
    messagebox.showinfo("Fertig", f"{moved_files} Dateien verschoben.")

# --------------------------
# GUI
root = tk.Tk()
root.title("Claptrap 0.4 – Dokumentensortierer mit Kategorie")

source_var = tk.StringVar()
target_var = tk.StringVar()
category_var = tk.StringVar(value="EÜR")  # Standardkategorie

# Quellordner
tk.Label(root, text="Quellordner:").grid(row=0, column=0, sticky="w")
tk.Entry(root, textvariable=source_var, width=50).grid(row=0, column=1)
tk.Button(root, text="Auswählen", command=select_source_folder).grid(row=0, column=2)

# Zielordner
tk.Label(root, text="Zielordner:").grid(row=1, column=0, sticky="w")
tk.Entry(root, textvariable=target_var, width=50).grid(row=1, column=1)
tk.Button(root, text="Auswählen", command=select_target_folder).grid(row=1, column=2)

# Kategorie-Auswahl
tk.Label(root, text="Kategorie:").grid(row=2, column=0, sticky="w")
tk.OptionMenu(root, category_var, "EÜR", "Privat").grid(row=2, column=1, sticky="w")

# Sortierbutton
tk.Button(root, text="Dateien sortieren", command=sort_files, bg="#4CAF50", fg="white").grid(row=3, column=1, pady=10)

# Regeln GUI
tk.Label(root, text="Regeln:").grid(row=4, column=0, sticky="nw")
rule_list = tk.Listbox(root, width=50, height=10)
rule_list.grid(row=4, column=1, columnspan=2, sticky="w")

# Buttons für Regeln
btn_frame = tk.Frame(root)
btn_frame.grid(row=5, column=1, columnspan=2, pady=5, sticky="w")
tk.Button(btn_frame, text="Hinzufügen", command=add_rule).pack(side="left", padx=2)
tk.Button(btn_frame, text="Bearbeiten", command=edit_rule).pack(side="left", padx=2)
tk.Button(btn_frame, text="Löschen", command=delete_rule).pack(side="left", padx=2)

update_rule_list()
root.mainloop()
