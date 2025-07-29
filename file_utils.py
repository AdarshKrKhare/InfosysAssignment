import os

def save_file(file) -> str:
    path = f"data/{file.filename}"
    with open(path, "wb") as buffer:
        buffer.write(file.file.read())
    return path
