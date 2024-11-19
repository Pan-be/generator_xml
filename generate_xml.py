
import pandas as pd
import xml.etree.ElementTree as ET

# load excel file
file_path = '/path_to_file/Opisy gier.xlsx'  # Replace path_to_file with the correct file path

df_lg = pd.read_excel(file_path, sheet_name='LG')

# Function to create an XML structure for one record
def create_xml_record(row):
    record = ET.Element('record')
    
    fields = {
        'Nazwa': row['Nazwa'],
        'SCD': row['SCD (zł)'],
        'Liczba': row['Liczba graczy'],
        'Czas': row['Czas gry w min'],
        'Wiek': row['Wiek graczy'],
        'OpisDługi': row['Długi opis'],
        'OpisKrótki': row['Krótki opis'],
        'EAN': row['Numer EAN'],
        'Wymiary': row['Wymiary (cm)'],
        'WymiaryZbiorcze': row['Wymiary zbiorczego (cm)'],
        'Waga': row['Waga (kg)'],
        'OpakowanieZbiorcze': row['Opakowanie zbiorcze (szt)'],
        'Kraj': row['Kraj pochodzenia']
    }
    
    for key, value in fields.items():
        element = ET.SubElement(record, key)
        element.text = str(value) if pd.notna(value) else ''
    
    return record

# Create a root XML element

root = ET.Element('records')

# Add each record to the main item

for _, row in df_lg.iterrows():
    root.append(create_xml_record(row))

# Create an XML tree and save to file

xml_file_path = '/path_to_file/gry.xml'  # Zreplace path_to_save with the correct path to save the file

tree = ET.ElementTree(root)
tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

print(f"XML file saved to: {xml_file_path}")
