import PyPDF2
from PyPDF2 import PdfMerger
from projects_low_complexity.secrets import get_secrets

def merge_pdfs(pdf_files, output_file):
    merger = PdfMerger()

    for pdf_file in pdf_files:
        merger.append(pdf_file)

    merger.write(output_file)
    merger.close()

# Example usage
file_path = get_secrets()
file1 = file_path['file1']
file2 = file_path['file2']
pdf_files = [file1, file2]
output_file = file_path['output_file']

merge_pdfs(pdf_files, output_file)
print("The pdf's have been merged successfully")
