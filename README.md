# Fixed-Width File Parser and Anonymizer
This repository contains a Python-based tool designed to parse fixed-width files using a given "**spec.json**" file and anonymize sensitive data in CSV files. My Goal is to provide Simple easy solution yet durable with data privacy.

**Table of Contents**

1. **Project Overview**

The Fixed-Width File Parser and Anonymizer is designed to handle fixed-width text files, where each column has a specified width given in **spec.json** file. It reads these files based on a configuration file that specifies the width of each column, then outputs the parsed data into a CSV file. Additionally, it includes functionality to anonymize specific fields, such as **first_name, last_name, and address**, to protect sensitive information.

2. **Features**
   
   **Flexible Parsing**: Define custom column widths using a specification file.
   
   **Data Anonymization**: Hash sensitive fields to anonymize data while maintaining its format.
   
   **Output to CSV**: Convert fixed-width files to CSV format for easier data manipulation and analysis.
   
   **Testing Suite**: Includes unit tests to verify the functionality of the parser and anonymizer.

## Installation

**Clone the Repository**

```python
git clone https://github.com/yourusername/fixed-width-parser-and-anonymizer.git
cd fixed-width-parser-and-anonymizer
```

**Set up a virtual environment**
```
python3 -m venv venv
source venv/bin/activate
```

**Install dependencies**
```
pip install -r requirements.txt
```
## Usage

**Parsing Fixed-Width Files**

To parse a fixed-width file:

   1. Place your fixed-width file in the data/ directory.

   2. Define the specification in a .txt file in the specs/ directory.

   3. Run the parser script:
```
python src/parser.py
```
This will generate a CSV file in the data/ directory based on the provided specification.

**Anonymizing Data**

To anonymize sensitive data in the CSV file:

   1. Ensure your parsed CSV file is in the data/ directory.

   2. Run the anonymizer script:
```
python src/anonymizer.py
```

The script will create an anonymized version of the CSV file, saving it in the data/ directory.


