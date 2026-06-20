def load_document(file_path: str) -> str:
    """
    Reads a text file and returns its contents.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()