import PyPDF2
from PyPDF2 import PdfMerger
import os

def merge_pdfs(pdf_files, output_file):
    merger = PdfMerger()

    for pdf_file in pdf_files:
        merger.append(pdf_file)

    merger.write(output_file)
    merger.close()

def get_pdf_files(folder_path):
    pdf_files = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            pdf_files.append(os.path.join(folder_path, filename))
    return pdf_files

def main():
    folder_path = input("Enter the folder path containing the PDFs to merge: ")
    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid folder path.")
        return

    pdf_files = get_pdf_files(folder_path)
    if pdf_files:
        output_file = input("Enter the file path for the merged PDF file: ")
        output_dir = os.path.dirname(output_file)
        try:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            merge_pdfs(pdf_files, output_file)
            print("The PDFs have been merged successfully.")
        except FileNotFoundError as fe:
            print("Invalid path: ", str(fe))
    else:
        print("No PDFs found in the folder.")

if __name__ == "__main__":
    main()
