import unittest
import tempfile
import shutil
from claptrap.core.file_sorter import sort_files

class TestFileSorter(unittest.TestCase):
    def setUp(self):
        import tempfile, shutil
        self.temp_source = tempfile.mkdtemp()
        self.temp_target = tempfile.mkdtemp()

        # so muss rules aussehen:
        self.rules = {
            "EÜR": {"category": "EÜR", "folder": "Rechnungen"},
            "Privat": {"category": "Privat", "folder": "Gehalt"},
        }

    def tearDown(self):
        import shutil
        shutil.rmtree(self.temp_source)
        shutil.rmtree(self.temp_target)

    def test_sort_files_moves_invoice(self):
        import os
        # Dummy-Datei erzeugen
        test_file = os.path.join(self.temp_source, "rechnung_EÜR.pdf")
        with open(test_file, "w") as f:
            f.write("Testinhalt")

        from claptrap.core.file_sorter import sort_files
        # Funktion ausführen
        sort_files(self.temp_source, self.temp_target, "EÜR", self.rules)

        # Erwarteter Pfad:
        expected_folder = os.path.join(self.temp_target, "Rechnungen")
        moved_file = os.path.join(expected_folder, "rechnung_EÜR.pdf")

        self.assertTrue(os.path.exists(moved_file))
