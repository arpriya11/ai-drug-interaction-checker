import ollama
from typing import Dict
import traceback

PROMPT_TEMPLATE = """
You are a helpful and safety-focused AI healthcare assistant.

Explain the interaction between the following two drugs in clear, non-technical terms: {query}

If there's any serious risk, flag it and explain simply.

Include a disclaimer like: "This is not medical advice. Always consult your doctor."

Do not make up facts. Keep the answer short and simple.
"""
print("✅ rag_pipeline_local.py loaded")

def get_interaction_explanation_local(query: str) -> Dict:
    print("🚀 Function called with query:", query)
        prompt = PROMPT_TEMPLATE.format(query=query)
        print("📨 Prompt sent to Ollama:\n", prompt)

        response = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": prompt}]
        )

        print("📥 Raw Ollama response:", response)

        if "message" not in response or "content" not in response["message"]:
            raise ValueError("Unexpected response format from Ollama: " + str(response))

        return {
            "answer": response.message.content.strip(),
            "sources": ["Ollama: mistral (local)"]
        }

    except Exception as e:
        print("❌ ERROR while calling Ollama:")
        traceback.print_exc()
        return {
            "answer": f"Something went wrong while generating a response using the local model:\n\n{str(e)}",
            "sources": ["(none)"]
        }
