import zipfile
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

def extract_docx_xml(docx_path, output_dir):
    with zipfile.ZipFile(docx_path, 'r') as docx:
        xml_files = [name for name in docx.namelist() if name.endswith('.xml')]
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        for xml_file in xml_files:
            with docx.open(xml_file) as file:
                tree = ET.parse(file)
                xml_str = minidom.parseString(ET.tostring(tree.getroot())).toprettyxml()
                
                output_path = os.path.join(output_dir, xml_file)
                output_file_dir = os.path.dirname(output_path)
                if not os.path.exists(output_file_dir):
                    os.makedirs(output_file_dir)
                
                with open(output_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(xml_str)




# Path to the .docx file
docx_path = 'GURBP-CO-240425-01-SA-R1  - Rubyplay Security Report (EN) V1.0.docx'
# Directory to save the extracted XML files
output_dir = 'extracted_xml.xml'

extract_docx_xml(docx_path, output_dir)
