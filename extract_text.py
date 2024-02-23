from pdfminer.high_level import extract_text

pdf_path = r'C:\Users\Aaditya Dawkar\Desktop\Only Up\Big\Assets\Introduction to system software.pdf'
output_file_path = r'C:\Users\Aaditya Dawkar\Desktop\Only Up\Big\Assets\extracted.txt'

extracted_text = extract_text(pdf_path)


with open(output_file_path, 'w', encoding='utf-8') as output_file1:
    output_file1.write(extracted_text)

print(f"Text extracted and saved to '{output_file_path}'")
