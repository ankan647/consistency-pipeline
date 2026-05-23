import os

def read_text_file(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read().strip()

def load_novel(novel_path: str) -> str:
    return read_text_file(novel_path)

def load_backstory(backstory_path: str) -> str:
    return read_text_file(backstory_path)
