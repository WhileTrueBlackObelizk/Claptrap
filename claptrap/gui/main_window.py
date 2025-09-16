# gui/main_window.py
# ------------------------------------------------------------
# Hauptfenster von Claptrap
# ------------------------------------------------------------
import tkinter as tk
from claptrap.core.rule_manager import load_rules
from claptrap.gui.file_sorter_gui import create_file_sorter_frame
from claptrap.gui.rule_editor import create_rule_editor_frame


import tkinter as tk

def show_welcome_popup(root):
    """
    Zeigt ein kleines Willkommens-Popup an, das weggeklickt werden kann.
    """
    popup = tk.Toplevel(root)
    popup.title("Willkommen bei Claptrap")
    popup.geometry("400x200")
    popup.configure(bg="#1E1E1E")  # dunkler Hintergrund passend zum Claptrap-Style
    popup.transient(root)  # bleibt über dem Hauptfenster
    popup.grab_set()       # blockiert Interaktion mit Hauptfenster

    # Nachricht
    tk.Label(popup, text="Willkommen bei Claptrap!\nDein Dokumentensortierer", 
             bg="#1E1E1E", fg="white", font=("Helvetica", 14)).pack(pady=30)

    # Schließen-Button
    tk.Button(popup, text="Los geht's!", bg="#4CAF50", fg="white", 
              command=popup.destroy).pack(pady=20)


def create_main_window():
    """
    Erstellt das Hauptfenster, integriert Unterframes und gibt root zurück.
    """
    root = tk.Tk()
    root.configure(bg="#1E1E1E")  # dunkles, technisches Claptrap-Feeling
    root.title("Claptrap 0.1 – Dokumentensortierer")
    root.geometry("900x700")  # Mindestgröße setzen
    root.minsize(700, 500)

    show_welcome_popup(root)
    
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
