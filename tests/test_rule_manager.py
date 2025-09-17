import json
import os
import tempfile
import unittest

from claptrap.core.rule_manager import load_rules, save_rules

class TestRuleManager(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()

        self.rules = [
            {"keyword": "rechnung", "target_folder": "Rechnungen", "category": "EÜR"},
            {"keyword": "gehalt", "target_folder": "Gehalt", "category": "Privat"},
        ]
        # Regeln in Datei speichern
        with open(self.temp_file.name, "w", encoding="utf-8") as f:
            json.dump(self.rules, f)

    def tearDown(self):
        os.remove(self.temp_file.name)

    def test_load_rules_returns_rules(self):
        """Test: load_rules lädt Regeln korrekt."""
        loaded_rules = load_rules(self.temp_file.name)
        self.assertEqual(len(loaded_rules), 2)
        self.assertEqual(loaded_rules[0]["keyword"], "rechnung")

    def test_save_rules_writes_rules(self):
        """Test: save_rules schreibt Regeln korrekt."""
        new_rules = [{"keyword": "vertrag", "target_folder": "Verträge", "category": "Privat"}]
        save_rules(new_rules, self.temp_file.name)
        loaded_rules = load_rules(self.temp_file.name)
        self.assertEqual(len(loaded_rules), 1)
        self.assertEqual(loaded_rules[0]["keyword"], "vertrag")

if __name__ == "__main__":
    unittest.main()
