import unittest
import os
from Index import Index


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.filename = 'testfile.txt'
        self.data = 'This is a test file.'

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_create_file(self):
        Index.create_file(self.filename, self.data)
        self.assertTrue(os.path.exists(self.filename))

    def test_add_data_to_file(self):
        Index.create_file(self.filename, self.data)
        Index.add_data_to_file(self.filename, self.data)
        with open(self.filename, 'r') as f:
            self.assertEqual(f.read(), self.data + self.data)

    def test_read_data_from_file(self):
        Index.create_file(self.filename, self.data)
        self.assertEqual(Index.read_data_from_file(self.filename), self.data)

    def test_overwrite_file(self):
        Index.create_file(self.filename, self.data)
        Index.overwrite_file(self.filename, self.data)
        with open(self.filename, 'r') as f:
            self.assertEqual(f.read(), self.data)

    def test_delete_file(self):
        Index.create_file(self.filename, self.data)
        Index.delete_file(self.filename)
        self.assertFalse(os.path.exists(self.filename))


if __name__ == '__main__':
    unittest.main()
