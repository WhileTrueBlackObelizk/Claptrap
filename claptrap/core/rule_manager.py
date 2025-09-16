# core/rule_manager.py
# ------------------------------------------------------------
# Funktionen zur Verwaltung der Regeln für Claptrap
# ------------------------------------------------------------

import json
import os

RULES_FILE = "rules.json"

# --------------------------
# Regeln laden / speichern

def load_rules():
    """
    Lädt die Regeln aus rules.json.
    Gibt ein Dictionary zurück.
    """
    if os.path.exists(RULES_FILE):
        with open(RULES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    # Standard-Regeln, falls Datei nicht existiert
    return {
        "rechnung": {"folder": "Rechnungen", "category": "EÜR"},
        "beleg": {"folder": "Belege", "category": "EÜR"},
        "kontoauszug": {"folder": "Kontoauszüge", "category": "EÜR"},
        "steuer": {"folder": "Steuerunterlagen", "category": "EÜR"},
        "gehalt": {"folder": "Gehalt", "category": "Privat"},
        "versicherung": {"folder": "Versicherungen", "category": "Privat"},
        "vertrag": {"folder": "Verträge", "category": "Privat"},
    }

def save_rules(rules):
    """
    Speichert das gegebene Regel-Dictionary in rules.json
    """
    with open(RULES_FILE, "w", encoding="utf-8") as f:
        json.dump(rules, f, indent=4, ensure_ascii=False)

# --------------------------
# Regeln bearbeiten

def add_rule(rules, keyword, folder, category):
    """
    Fügt eine neue Regel hinzu.
    """
    rules[keyword.lower()] = {"folder": folder, "category": category}
    save_rules(rules)

def edit_rule(rules, old_keyword, new_keyword, new_folder, new_category):
    """
    Bearbeitet eine bestehende Regel.
    """
    if old_keyword in rules:
        del rules[old_keyword]
    rules[new_keyword.lower()] = {"folder": new_folder, "category": new_category}
    save_rules(rules)

def delete_rule(rules, keyword):
    """
    Löscht eine Regel.
    """
    if keyword in rules:
        del rules[keyword]
        save_rules(rules)
