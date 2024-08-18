This script will anonymize sensitive columns (f1, f2, f3, etc.) by hashing them.

```
import pandas as pd
import hashlib

def hash_field(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def anonymize_csv(input_file, output_file, columns_to_anonymize):
    df = pd.read_csv(input_file)
    
    for column in columns_to_anonymize:
        df[column] = df[column].apply(hash_field)
    
    df.to_csv(output_file, index=False)
    print(f"Data anonymized and saved to {output_file}")

if __name__ == "__main__":
    input_file = 'data/output.csv'
    output_file = 'data/anonymized_output.csv'
    columns_to_anonymize = ['f1', 'f2', 'f3']  # Adjust columns as needed
    anonymize_csv(input_file, output_file, columns_to_anonymize)

```
