import subprocess

def transcribe_audio(file_path: str) -> str:
    output_file = file_path.replace(".wav", ".txt")
    subprocess.run(["./whisper.cpp/main", "-f", file_path, "-otxt"])
    with open(output_file, "r") as f:
        return f.read()
