import os
import shutil
import tempfile
import unittest

from claptrap.utils.helpers import ensure_folder

class TestHelpers(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.folder_path = os.path.join(self.temp_dir, "new_folder")

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_ensure_folder_creates_directory(self):
        """Test: ensure_folder legt Ordner an."""
        self.assertFalse(os.path.exists(self.folder_path))
        ensure_folder(self.folder_path)
        self.assertTrue(os.path.exists(self.folder_path))

if __name__ == "__main__":
    unittest.main()
