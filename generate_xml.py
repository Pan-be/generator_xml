
import pandas as pd
import xml.etree.ElementTree as ET

# Wczytaj plik Excel
file_path = '/home/kbieniek/Desktop/Lucrum/Opisy gier.xlsx'  # Zastąp 'path_to_your_file' właściwą ścieżką do pliku
df_lg = pd.read_excel(file_path, sheet_name='LG')

# Funkcja do utworzenia struktury XML dla jednego rekordu
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

# Utwórz główny element XML
root = ET.Element('records')

# Dodaj każdy rekord do głównego elementu
for _, row in df_lg.iterrows():
    root.append(create_xml_record(row))

# Utwórz drzewo XML i zapisz do pliku
xml_file_path = '/home/kbieniek/Desktop/Lucrum/gry.xml'  # Zastąp 'path_to_save' właściwą ścieżką do zapisu pliku
tree = ET.ElementTree(root)
tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

print(f"XML file saved to: {xml_file_path}")
