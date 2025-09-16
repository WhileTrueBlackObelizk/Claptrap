# claptrap.py
# ------------------------------------------------------------
# Startpunkt der Claptrap-Anwendung
# ------------------------------------------------------------
# claptrap.py
import tkinter as tk
from claptrap.gui.main_window import create_main_window  # <- wichtig
from claptrap.core.rule_manager import *

if __name__ == "__main__":
    # Hauptfenster erstellen
    root = create_main_window()
    
    # App starten
    root.mainloop()
