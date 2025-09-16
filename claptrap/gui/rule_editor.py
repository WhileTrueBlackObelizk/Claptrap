# gui/rule_editor.py
# ------------------------------------------------------------
# GUI für die Verwaltung der Regeln
# ------------------------------------------------------------

import tkinter as tk
from tkinter import messagebox, simpledialog
from claptrap.core.rule_manager import add_rule, edit_rule, delete_rule, save_rules

def create_rule_editor_frame(root, rules):
    """
    Erstellt den Frame für die Regel-Liste und die Buttons.
    Gibt den Frame zurück (wird im Hauptfenster gepackt).
    """
    frame = tk.Frame(root)
    
    # Listbox für Regeln
    tk.Label(frame, text="Regeln:").grid(row=0, column=0, sticky="nw")
    rule_list = tk.Listbox(frame, width=50, height=10)
    rule_list.grid(row=0, column=1, columnspan=2, sticky="w")

    # Buttons
    btn_frame = tk.Frame(frame)
    btn_frame.grid(row=1, column=1, columnspan=2, pady=5, sticky="w")
    tk.Button(btn_frame, text="Hinzufügen", command=lambda: add_rule_gui(rule_list, rules)).pack(side="left", padx=2)
    tk.Button(btn_frame, text="Bearbeiten", command=lambda: edit_rule_gui(rule_list, rules)).pack(side="left", padx=2)
    tk.Button(btn_frame, text="Löschen", command=lambda: delete_rule_gui(rule_list, rules)).pack(side="left", padx=2)

    update_rule_list(rule_list, rules)
    return frame  # NICHT packen hier

# --------------------------
# Hilfsfunktionen für GUI

def update_rule_list(rule_list, rules):
    rule_list.delete(0, tk.END)
    for k, v in rules.items():
        rule_list.insert(tk.END, f"{k} → {v['folder']} ({v['category']})")
        color = "#81C784" if v["category"] == "EÜR" else "#E57373"
        rule_list.itemconfig(tk.END, {'fg': color})

def add_rule_gui(rule_list, rules):
    keyword = simpledialog.askstring("Neue Regel", "Schlüsselwort:")
    if not keyword: return
    folder = simpledialog.askstring("Neue Regel", "Zielordner:")
    if not folder: return
    category = simpledialog.askstring("Neue Regel", "Kategorie (EÜR oder Privat):", initialvalue="EÜR")
    if category not in ["EÜR", "Privat"]:
        messagebox.showwarning("Kategorie", "Kategorie muss 'EÜR' oder 'Privat' sein.")
        return
    add_rule(rules, keyword, folder, category)
    update_rule_list(rule_list, rules)

def edit_rule_gui(rule_list, rules):
    selected = rule_list.curselection()
    if not selected:
        messagebox.showwarning("Bearbeiten", "Bitte eine Regel auswählen")
        return
    old_keyword = rule_list.get(selected[0]).split(" → ")[0]
    rule = rules[old_keyword]
    new_keyword = simpledialog.askstring("Bearbeiten", "Neues Schlüsselwort:", initialvalue=old_keyword)
    if not new_keyword: return
    new_folder = simpledialog.askstring("Bearbeiten", "Neuer Zielordner:", initialvalue=rule["folder"])
    if not new_folder: return
    new_category = simpledialog.askstring("Bearbeiten", "Kategorie (EÜR oder Privat):", initialvalue=rule["category"])
    if new_category not in ["EÜR", "Privat"]:
        messagebox.showwarning("Kategorie", "Kategorie muss 'EÜR' oder 'Privat' sein.")
        return
    edit_rule(rules, old_keyword, new_keyword, new_folder, new_category)
    update_rule_list(rule_list, rules)

def delete_rule_gui(rule_list, rules):
    selected = rule_list.curselection()
    if not selected:
        messagebox.showwarning("Löschen", "Bitte eine Regel auswählen")
        return
    keyword = rule_list.get(selected[0]).split(" → ")[0]
    if messagebox.askyesno("Löschen", f"Regel '{keyword}' wirklich löschen?"):
        delete_rule(rules, keyword)
        update_rule_list(rule_list, rules)
