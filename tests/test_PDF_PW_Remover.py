import os
import PDF_PW_Remover


def test_remove_password():
    pdf_file = "sample_password_protected.pdf"
    output_folder = "output_test"
    PDF_PW_Remover.remove_password(pdf_file, output_folder)
    assert os.path.exists(os.path.join(output_folder, os.path.basename(pdf_file)))


def test_remove_passwords_in_folder():
    input_folder = "input_test"
    output_folder = "output_test"
    PDF_PW_Remover.remove_passwords_in_folder(input_folder, output_folder)
    assert os.listdir(output_folder)


if __name__ == "__main__":
    test_remove_password()
    test_remove_passwords_in_folder()
