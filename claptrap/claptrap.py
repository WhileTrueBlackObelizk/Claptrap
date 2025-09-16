# ------------------------------------------------------------
# Claptrap – Dein smarter Dokumentensortierer
# Version 0.2
#
# Dieses Programm nimmt Dateien aus einem Quellordner und
# verschiebt sie automatisch in Unterordner eines Zielordners,
# basierend auf Schlüsselwörtern im Dateinamen.
#
# Jetzt mit erweiterten Kategorien für EÜR und Privat.
# ------------------------------------------------------------

# --- BENÖTIGTE MODULE LADEN ---
import os                      # Zum Arbeiten mit Dateien und Ordnern
import shutil                  # Zum Verschieben und Kopieren von Dateien
import tkinter as tk           # GUI-Bibliothek für Fenster, Buttons, Eingabefelder
from tkinter import filedialog, messagebox  # Für Ordnerauswahl und Pop-up-Meldungen

# ------------------------------------------------------------
# REGELWERK
# ------------------------------------------------------------
# Format: "schlüsselwort_im_dateinamen": "Zielordnername/Unterordnername"
# So werden Dateien nach Schlüsselwort in Unterordner verschoben.

rules = {
    # --- EÜR (geschäftlich) ---
    "rechnung": "EÜR/Rechnungen",
    "beleg": "EÜR/Belege",           # alles mit 'beleg' landet hier (geschäftlich)
    "kontoauszug": "EÜR/Kontoauszüge",

    # --- Privat ---
    "privatbeleg": "Privat/Belege",  # wenn du unterscheiden willst, sonst gleiche Keywords
    "gehalt": "Privat/Gehalt",
    "versicherung": "Privat/Versicherungen",

    # --- Sonstiges sinnvolles Beispiel ---
    "vertrag": "Privat/Verträge",
    "steuer": "EÜR/Steuerunterlagen",
}

# Hinweis:
# - Das Programm prüft nur auf die Schlüsselwörter im Dateinamen.
# - Du kannst jederzeit neue Regeln hinzufügen oder bestehende ändern.
# - Schreib die Schlüsselwörter klein; im Code wird alles kleingeschrieben geprüft.

# ------------------------------------------------------------
# FUNKTIONEN
# ------------------------------------------------------------

def select_source_folder():
    """
    Öffnet ein Dialogfenster, in dem du den Quellordner auswählen kannst.
    Der Pfad wird dann in source_var gespeichert.
    """
    folder = filedialog.askdirectory(title="Quellordner auswählen")
    if folder:
        source_var.set(folder)

def select_target_folder():
    """
    Öffnet ein Dialogfenster, in dem du den Zielordner auswählen kannst.
    Der Pfad wird dann in target_var gespeichert.
    """
    folder = filedialog.askdirectory(title="Zielordner auswählen")
    if folder:
        target_var.set(folder)

def sort_files():
    """
    Hauptfunktion: sortiert Dateien aus dem Quellordner
    anhand der Schlüsselwörter in 'rules' in Unterordner des Zielordners.
    """
    source_folder = source_var.get()
    target_folder = target_var.get()

    if not source_folder or not target_folder:
        messagebox.showwarning("Fehler", "Bitte Quell- und Zielordner auswählen.")
        return

    moved_files = 0

    # Alle Dateien im Quellordner durchgehen
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)

        if os.path.isfile(file_path):
            file_lower = file.lower()

            # Regeln durchgehen
            for keyword, folder_name in rules.items():
                if keyword in file_lower:
                    # Zielordner (Unterordner) erstellen
                    dest_folder = os.path.join(target_folder, folder_name)
                    os.makedirs(dest_folder, exist_ok=True)

                    # Datei verschieben
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    moved_files += 1
                    break

    messagebox.showinfo("Fertig", f"{moved_files} Dateien verschoben.")

# ------------------------------------------------------------
# GUI (GRAPHICAL USER INTERFACE)
# ------------------------------------------------------------

root = tk.Tk()
root.title("Claptrap – Dokumentensortierer")

# Variablen für Quell- und Zielordner
source_var = tk.StringVar()
target_var = tk.StringVar()

# Quellordner
tk.Label(root, text="Quellordner:").grid(row=0, column=0, sticky="w")
tk.Entry(root, textvariable=source_var, width=50).grid(row=0, column=1)
tk.Button(root, text="Auswählen", command=select_source_folder).grid(row=0, column=2)

# Zielordner
tk.Label(root, text="Zielordner:").grid(row=1, column=0, sticky="w")
tk.Entry(root, textvariable=target_var, width=50).grid(row=1, column=1)
tk.Button(root, text="Auswählen", command=select_target_folder).grid(row=1, column=2)

# Sortierbutton
tk.Button(
    root,
    text="Dateien sortieren",
    command=sort_files,
    bg="#4CAF50", fg="white"
).grid(row=2, column=1, pady=10)

# Hauptschleife starten
root.mainloop()

# ------------------------------------------------------------
# ANWENDUNG
# ------------------------------------------------------------
# 1. Skript starten → Fenster öffnet sich.
# 2. Quellordner auswählen (z.B. Downloads).
# 3. Zielordner auswählen (z.B. „Meine Dokumente/Steuer“).
# 4. Auf "Dateien sortieren" klicken.
# 5. Claptrap verschiebt alle Dateien nach den oben definierten Regeln
#    in Unterordner (z.B. EÜR/Rechnungen, Privat/Gehalt usw.).
# ------------------------------------------------------------
# Viel Erfolg bei der Organisation deiner Dokumente!