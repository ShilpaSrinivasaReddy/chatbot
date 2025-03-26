# parse_pdfs.py
import fitz
import os

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    return "\n".join([page.get_text() for page in doc])

def extract_all_pdfs(data_dir='data'):
    all_texts = []
    for file in os.listdir(data_dir):
        if file.endswith('.pdf'):
            text = extract_text_from_pdf(os.path.join(data_dir, file))
            all_texts.append(text)
    return "\n".join(all_texts)

if __name__ == "__main__":
    full_text = extract_all_pdfs()
    with open("data/full_text.txt", "w") as f:
        f.write(full_text)
    print("✅ PDF parsing complete. Text saved to data/full_text.txt")
