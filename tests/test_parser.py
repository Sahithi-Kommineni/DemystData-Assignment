We can test the code using below script

```
import unittest
import os
import pandas as pd
from src.anonymizer import anonymize_csv

class TestAnonymizer(unittest.TestCase):

    def setUp(self):
        self.input_file = 'data/test_output.csv'
        self.output_file = 'data/test_anonymized_output.csv'
        self.columns_to_anonymize = ['f1', 'f2', 'f3']
    
    def test_anonymize_csv(self):
        anonymize_csv(self.input_file, self.output_file, self.columns_to_anonymize)
        self.assertTrue(os.path.exists(self.output_file))

        df = pd.read_csv(self.output_file)
        for column in self.columns_to_anonymize:
            self.assertNotEqual(df[column][0], 'original_value')  # Adjust 'original_value' based on your data
    
    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

if __name__ == '__main__':
    unittest.main()
```
