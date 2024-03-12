import PyPDF2
from PyPDF2 import PdfMerger
import os

def merge_pdfs(pdf_files, output_file):
    merger = PdfMerger()

    for pdf_file in pdf_files:
        merger.append(pdf_file)

    merger.write(output_file)
    merger.close()

def get_input_files():
    pdf_files = []
    while True:
        file_path = input("Enter the file path of a PDF to merge (or type 'done' to finish): ")
        if file_path == 'done'.lower():
            break
        elif not os.path.isfile(file_path):
            print(f"Error: '{file_path}' is not a valid file path.")
        else:
            if file_path.lower().endswith('.pdf'):
                pdf_files.append(file_path)
            else:
                print(f"Error: '{file_path}' is not a PDF file.")
    return pdf_files

def main():
    input_files = get_input_files()
    if input_files:
        output_file = input("Enter the file path for the merged PDF file: ")
        output_dir = os.path.dirname(output_file)
        try:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            merge_pdfs(input_files, output_file)
            print("The PDFs have been merged successfully.")
        except FileNotFoundError as fe:
            print("Invalid path: ", str(fe))
    else:
        print("No PDFs to merge.")

if __name__ == "__main__":
    main()
