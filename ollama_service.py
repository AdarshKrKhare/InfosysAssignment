import requests

OLLAMA_API = "http://localhost:11434/api/generate"
MODEL = "llama2"

def generate_response(question: str, context: str) -> str:
    prompt = f"""
    Context:
    {context}

    Question: {question}
    Answer:"""

    response = requests.post(OLLAMA_API, json={"model": MODEL, "prompt": prompt, "stream": False})
    return response.json().get("response", "No response")
