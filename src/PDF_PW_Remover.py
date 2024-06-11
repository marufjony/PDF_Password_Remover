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
                    print(f"Password removed from {pdf_file}.")
                else:
                    print(f"No password found for {pdf_file}.")
            except Exception as e:
                print(f"Error processing {pdf_file}: {str(e)}")

def remove_password_in_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_file = os.path.join(input_folder, filename)
            remove_password(pdf_file, output_folder)

if __name__ == "__main__":
    input_folder = "input_pdfs"
    output_folder = "output_pdfs"
    remove_passwords_in_folder(input_folder, output_folder)
