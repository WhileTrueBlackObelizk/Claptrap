# utils/helpers.py
# ------------------------------------------------------------
# Kleine Hilfsfunktionen für Claptrap
# ------------------------------------------------------------

import os
from datetime import datetime

# --------------------------
# Pfad-Utilities

def ensure_folder(path):
    """
    Prüft, ob ein Ordner existiert, sonst erstellen
    """
    os.makedirs(path, exist_ok=True)
    return path

def is_valid_folder(path):
    """
    Prüft, ob ein Pfad ein existierender Ordner ist
    """
    return os.path.exists(path) and os.path.isdir(path)

# --------------------------
# Farb-Utilities

def get_category_color(category):
    """
    Gibt die Farbe für die Kategorie zurück
    """
    colors = {
        "EÜR": "green",
        "Privat": "blue"
    }
    return colors.get(category, "black")

# --------------------------
# Datums-/Zeit-Utilities

def current_timestamp():
    """
    Gibt die aktuelle Zeit als String zurück
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --------------------------
# Sonstige kleine Helfer

def sanitize_filename(filename):
    """
    Entfernt unerwünschte Zeichen aus Dateinamen
    """
    return "".join(c for c in filename if c.isalnum() or c in " .-_")
