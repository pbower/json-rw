import unittest
import os
from better_json import read_json, write_json

class TestCustomJsonHandler(unittest.TestCase):

    def setUp(self):
        """Set up test variables."""
        self.test_data = {"name": "Test", "value": 42}
        self.test_file = "test_output.json"

    def tearDown(self):
        """Clean up the created test file after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_write_json(self):
        """Test if write_json correctly writes data to a file."""
        write_json(self.test_data, self.test_file)
        self.assertTrue(os.path.exists(self.test_file), "File was not created.")

    def test_read_json(self):
        """Test if read_json correctly reads data from a file."""
        write_json(self.test_data, self.test_file)
        data = read_json(self.test_file)
        self.assertEqual(data, self.test_data, "Data read from file does not match the original.")

if __name__ == "__main__":
    unittest.main()
