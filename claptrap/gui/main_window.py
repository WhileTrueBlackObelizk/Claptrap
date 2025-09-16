# gui/main_window.py
# ------------------------------------------------------------
# Hauptfenster von Claptrap
# ------------------------------------------------------------
import tkinter as tk
from core.rule_manager import load_rules
from gui.file_sorter_gui import create_file_sorter_frame
from gui.rule_editor import create_rule_editor_frame

def create_main_window():
    """
    Erstellt das Hauptfenster, integriert Unterframes und gibt root zurück.
    """
    root = tk.Tk()
    root.configure(bg="#1E1E1E")  # dunkles, technisches Claptrap-Feeling
    root.title("Claptrap 0.5 – Dokumentensortierer")
    root.geometry("900x700")  # Mindestgröße setzen
    root.minsize(700, 500)

    # Regeln laden
    rules = load_rules()
    
    # Frames erstellen und packen
    sorter_frame = create_file_sorter_frame(root, rules)
    sorter_frame.configure(bg="#2B2B2B")  # leicht dunkler als Hintergrund
    sorter_frame.pack(pady=10, fill="x")

    rule_frame = create_rule_editor_frame(root, rules)
    rule_frame.configure(bg="#2B2B2B")
    rule_frame.pack(pady=10, fill="x")


    return root
