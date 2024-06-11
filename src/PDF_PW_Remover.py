import os
import PyPDF2

def remove_password(pdf_file, output_dir):
    try:
        with open(pdf_file, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            if pdf_reader.is_encrypted:
                pdf_reader.decrypt('')
                output_path = os.path.join(output_dir, os.path.basename(pdf_file))
                with open(output_path, 'wb') as output_file:
                    pdf_writer = PyPDF2.PdfWriter()
                    for page_num in range(len(pdf_reader.pages)):
                        pdf_writer.add_page(pdf_reader.pages[pages_num])
                        pdf_writer.write(output_file)

