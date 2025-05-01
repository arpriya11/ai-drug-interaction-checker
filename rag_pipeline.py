import os
import openai
import chromadb
from typing import Dict
from dotenv import load_dotenv
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set OpenAI API key for chat model
openai.api_key = OPENAI_API_KEY

# Set up embedding function
embedding_fn = OpenAIEmbeddingFunction(api_key=OPENAI_API_KEY, model_name="text-embedding-ada-002")

# Initialize ChromaDB client and collection
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="drug_interactions", embedding_function=embedding_fn)

# Prompt Template
PROMPT_TEMPLATE = """
You are a helpful and safety-focused AI healthcare assistant.

Explain the interaction between the following two drugs in clear, non-technical terms: {query}

If there's any serious risk, flag it and explain simply.

Include a disclaimer like: "This is not medical advice. Always consult your doctor."

Only answer based on verified documents, and cite sources if available.
"""

def get_interaction_explanation(query: str) -> Dict:
    try:
        print("STEP 1: Querying vector DB...")
        results = collection.query(query_texts=[query], n_results=3)
        print("ChromaDB query results:", results)

        context_docs = results.get("documents", [[]])[0]
        sources = results.get("metadatas", [[]])[0]
        context = "\n\n".join(context_docs)
        source_names = [s.get("source", "Unknown") for s in sources]

        print("STEP 2: Generating prompt...")
        full_prompt = PROMPT_TEMPLATE.format(query=query) + f"\n\nContext:\n{context}"
        print("Prompt:\n", full_prompt)

        print("STEP 3: Sending to OpenAI...")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": full_prompt}],
            temperature=0.4
        )
        print("OpenAI responded.")

        answer = response.choices[0].message.content.strip()

        return {
            "answer": answer,
            "sources": list(set(source_names))
        }

    except Exception as e:
        import traceback
        print(f"❌ ERROR: {e}")
        print(traceback.format_exc())
        return {
            "answer": "Something went wrong while generating a response.",
            "sources": []
        }
