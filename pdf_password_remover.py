<<<<<<< HEAD
import os
import pikepdf

# Prompt the user for the directory and password
directory = input("Enter the directory containing the PDFs: ")
pdf_pass = input("Enter the password for the PDFs: ")

# Check if the directory exists
if not os.path.exists(directory):
    print(f"Error: The directory {directory} does not exist.")
else:
    # List all PDF files in the directory
    pdf_files = [f for f in os.listdir(directory) if f.endswith(".pdf")]

    # Process each PDF file
    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory, pdf_file)

        # Check if the path is a file
        if os.path.isfile(pdf_path):
            try:
                # Open the PDF with the password
                with pikepdf.open(pdf_path, password=pdf_pass) as pdf:
                    # Create a new filename for the password-free PDF
                    output_pdf_path = os.path.join(directory, f"unlocked_{pdf_file}")

                    # Save the password-free PDF
                    pdf.save(output_pdf_path)

                print(f"Password removed for {pdf_file}. Saved as {output_pdf_path}.")
            except pikepdf._qpdf.PasswordError:
                print(f"Skipping {pdf_file}: No password required.")
            except Exception as e:
                print(f"Failed to process {pdf_file}: {e}")
        else:
            print(f"Skipping {pdf_path}: Not a valid file.")
=======
import pikepdf

pdf_loc = input("PDF location: ")
pdf_pass = input("PDF password: ")

pdf = pikepdf.open(pdf_loc, password=pdf_pass)

print("\nProcessing...\n")

pdf_save = input("Save file as: ")
pdf_loc2 = input("Save location: ")

pdf.save(pdf_loc2 + '\\' + pdf_save)

print("The password successfully removed from the PDF")
print("\aLocation: " + pdf_loc + '\\' + pdf_save)
>>>>>>> 83abb0d1e3f94da3d66c46e2a1cb7d568cf7762e
