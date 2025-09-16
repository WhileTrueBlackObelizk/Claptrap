# core/file_sorter.py
# ------------------------------------------------------------
# Funktionen zum Sortieren und Verschieben von Dateien
# ------------------------------------------------------------
import os
import shutil
from utils.helpers import ensure_folder

def get_files_in_folder(folder):
    """
    Gibt alle Dateien in einem Ordner zurück
    """
    return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

def check_category_match(file_name, rule, category):
    """
    Prüft, ob die Datei zum Schlüsselwort und zur Kategorie passt
    """
    return rule["category"] == category and rule["keyword"].lower() in file_name.lower()

def move_file(file_path, target_folder):
    """
    Verschiebt eine einzelne Datei in den Zielordner
    """
    os.makedirs(target_folder, exist_ok=True)
    shutil.move(file_path, os.path.join(target_folder, os.path.basename(file_path)))

def sort_files(source_folder, target_folder, category, rules):
    """
    Sortiert alle Dateien aus dem Quellordner in Unterordner des Zielordners
    basierend auf Regeln und gewählter Kategorie.

    Parameter:
    - source_folder: Pfad zum Quellordner
    - target_folder: Pfad zum Zielordner
    - category: "EÜR" oder "Privat"
    - rules: dict der Regeln, z.B. { "rechnung": {"folder": "Rechnungen", "category": "EÜR"} }
    
    Rückgabe:
    - moved_files: Anzahl verschobener Dateien
    """
    moved_files = 0
    for file in get_files_in_folder(source_folder):
        file_path = os.path.join(source_folder, file)
        for keyword, rule in rules.items():
            if rule["category"] != category:
                continue
            if keyword.lower() in file.lower():
                dest_folder = os.path.join(target_folder, rule["folder"])
                move_file(file_path, dest_folder)
                moved_files += 1
                break  # Datei verschoben, nächste Datei
    return moved_files