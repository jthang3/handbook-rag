import ollama

def ask_llm(prompt):
    response = ollama.chat(
        model="llama3.2",
        messages=[{
            "role": "user",
            "content": prompt
        }],
        options={"temperature": 0.1}
    )
    return response["message"]["content"]