# Excel to XML Generator

This project is a Python script that generates an XML file from a specific sheet in an Excel workbook. It processes data from the sheet named **LG** and outputs it as an XML file.

## Features

- Converts the **LG** sheet of the provided Excel file into XML format.
- Ensures proper mapping of Excel columns to XML elements.
- Handles empty or missing values gracefully.

## Prerequisites

- Python 3.12 or higher installed on your system.
- Required Python packages:
  - `pandas`
  - `openpyxl`

## Installation

1. Clone this repository:
```bash
   git clone https://github.com/your-username/excel-to-xml-generator.git
   cd excel-to-xml-generator
```
2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```
3. Install the required dependencies:
```bash
pip install pandas openpyxl
```

# Usage

1. Place the Excel file to be processed in the project directory.

2. Open generate_xml.py and update the file path to your Excel file in the variable:
```python
file_path = '/path/to/your/excel/file.xlsx'
```
3. Run the script:
```bash
python generate_xml.py
```
4. The generated XML file will be saved in the specified output path:
```python
output_path = '/path/to/save/xml/file.xml'
```

## Customization

You can modify the column-to-XML mapping by editing the create_xml_record function in generate_xml.py.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
