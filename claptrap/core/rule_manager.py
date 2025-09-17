# core/rule_manager.py
# ------------------------------------------------------------
# Funktionen zur Verwaltung der Regeln für Claptrap
# ------------------------------------------------------------

import json
import os

RULES_FILE = os.path.join(os.path.dirname(__file__), "..", "rules.json")

def load_rules(file_path=None):
    """Lädt Regeln aus JSON-Datei."""
    path = file_path if file_path else RULES_FILE
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_rules(rules, file_path=None):
    """Speichert Regeln in JSON-Datei."""
    path = file_path if file_path else RULES_FILE
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rules, f, indent=4)


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
