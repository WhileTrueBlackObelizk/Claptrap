# claptrap.py
# ------------------------------------------------------------
# Startpunkt der Claptrap-Anwendung
# ------------------------------------------------------------

from gui.main_window import create_main_window  

if __name__ == "__main__":
    # Hauptfenster erstellen
    root = create_main_window()
    
    # App starten
    root.mainloop()
