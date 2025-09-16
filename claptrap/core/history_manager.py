# core/history_manager.py
# ------------------------------------------------------------
# Funktionen für Historie / Logging der verschobenen Dateien
# ------------------------------------------------------------

import json
import os
from datetime import datetime

HISTORY_FILE = "history.json"

def load_history():
    """
    Lädt die Historie aus der Datei. Gibt eine Liste von Einträgen zurück.
    """
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_history(history):
    """
    Speichert die Historie in die Datei.
    """
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)

def add_history_entry(file_name, source, target, category):
    """
    Fügt einen neuen Eintrag zur Historie hinzu.
    """
    history = load_history()
    entry = {
        "file_name": file_name,
        "source": source,
        "target": target,
        "category": category,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    history.append(entry)
    save_history(history)

def get_recent_entries(n=10):
    """
    Gibt die letzten n Einträge zurück (neueste zuerst)
    """
    history = load_history()
    return history[-n:][::-1]
