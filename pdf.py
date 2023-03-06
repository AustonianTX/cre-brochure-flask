from pypdf import PdfReader


def extract_text(file_path):
    reader = PdfReader(file_path)

    text = ''

    for i in range(len(reader.pages)):
        text += reader.pages[i].extract_text()
        text += '\n'

    return text
