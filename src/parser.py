This script reads the fixed-width file using the provided Spec.json file and outputs it as a CSV.

```
import json
import pandas as pd

def parse_fixed_width_file(spec_file, input_file, output_file):
                                                                                          # Load the specification from the JSON file
    with open(spec_file, 'r') as f:
        spec = json.load(f)
    
                                                                                          # Extract column names and offsets
    column_names = spec['ColumnNames']
    offsets = [int(offset) for offset in spec['Offsets']]
    fixed_width_encoding = spec.get('FixedWidthEncoding', 'utf-8')
    include_header = spec.get('IncludeHeader', 'True') == 'True'
    delimited_encoding = spec.get('DelimitedEncoding', 'utf-8')
    
                                                                                          # Read the fixed-width file
    df = pd.read_fwf(input_file, widths=offsets, names=column_names, encoding=fixed_width_encoding, header=0 if include_header else None)
    
    # Write to CSV
    df.to_csv(output_file, index=False, encoding=delimited_encoding)
    print(f"File parsed successfully and saved to {output_file}")

if __name__ == "__main__":
    spec_file = 'specs/Spec.json'
    input_file = 'data/sample_input.txt'
    output_file = 'data/output.csv'
    parse_fixed_width_file(spec_file, input_file, output_file)

```
