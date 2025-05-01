import ollama
from typing import Dict

# Local prompt template
PROMPT_TEMPLATE = """
You are a helpful and safety-focused AI healthcare assistant.

Explain the interaction between the following two drugs in clear, non-technical terms: {query}

If there's any serious risk, flag it and explain simply.

Include a disclaimer like: "This is not medical advice. Always consult your doctor."

Do not make up facts. Keep the answer short and simple.
"""

def get_interaction_explanation_local(query: str) -> Dict:
    try:
        prompt = PROMPT_TEMPLATE.format(query=query)
        print("📨 Sending prompt to Ollama:\n", prompt)

        # Query the local model
        response = ollama.chat(
            model="mistral",  # or another model like llama3, gemma, etc.
            messages=[{"role": "user", "content": prompt}]
        )

        print("📥 Response from Ollama:", response)

        return {
            "answer": response["message"]["content"].strip(),
            "sources": ["Ollama: mistral (local)"]
        }

    except Exception as e:
        print(f"❌ Ollama error: {e}")
        return {
            "answer": "Something went wrong while generating a response using the local model.",
            "sources": []
        }
