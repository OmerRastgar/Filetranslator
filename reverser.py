import zipfile
import os

# def extract_docx(docx_path, output_dir):
#     with zipfile.ZipFile(docx_path, 'r') as docx:
#         docx.extractall(output_dir)

# # Path to the .docx file
# docx_path = 'GURBP-CO-240425-01-SA-R1  - Rubyplay Security Report (EN) V1.0.docx'
# # Directory to save the extracted content
# output_dir = 'extracted_docx_2'
    
# extract_docx(docx_path, output_dir)


def create_docx_from_dir(input_dir, output_docx_path):
    with zipfile.ZipFile(output_docx_path, 'w', zipfile.ZIP_DEFLATED) as docx:
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                file_path = os.path.join(root, file)
                archive_name = os.path.relpath(file_path, input_dir)
                docx.write(file_path, archive_name)

# Directory containing the extracted content
input_dir = 'extracted_docx_2'
# Path to save the new .docx file
output_docx_path = 'recreated_document.docx'

create_docx_from_dir(input_dir, output_docx_path)
