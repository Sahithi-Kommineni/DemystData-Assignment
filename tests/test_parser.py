These scripts will contain unit tests for the parser and anonymizer to ensure they work correctly.

```
import unittest
import os
from src.parser import parse_fixed_width_file

class TestParser(unittest.TestCase):

    def setUp(self):
        self.spec_file = 'specs/Spec.json'
        self.input_file = 'data/sample_input.txt'
        self.output_file = 'data/test_output.csv'
    
    def test_parse_fixed_width_file(self):
        parse_fixed_width_file(self.spec_file, self.input_file, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

if __name__ == '__main__':
    unittest.main()

```
