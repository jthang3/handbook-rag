from pathlib import Path

def load_all_documents(path):
    file_path = Path(path)
    documents = []
    for file_info in file_path.iterdir():
        file_name = file_info.name
        file_text = file_info.read_text(encoding="utf-8")
        document = {
            "source": file_name,
            "text": file_text
        }
        documents.append(document)
    return documents
files = load_all_documents(Path(__file__).parent.parent/"doc")