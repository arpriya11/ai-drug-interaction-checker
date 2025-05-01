#ai-drug-interaction-checker
A Generative AI tool to explain drug interactions in simple language.

This project is a local AI-powered app that explains drug interactions in simple, non-technical language. It helps non-experts understand the risks of combining medications, powered entirely by:

🖥️ Ollama + Mistral (runs locally, offline)

🚀 Features

Natural language query input (e.g., "Can I take ibuprofen with fluoxetine?")

AI-generated, layman-friendly response

Includes a safety disclaimer

Fully local mode via Ollama (no internet required)

🗂 Folder Structure

drug-interaction-checker/
├── app.py                   # Local version using Ollama
├── rag_pipeline_local.py    # Ollama model logic
├── requirements.txt         # Python dependencies
└── .streamlit

🔧 Local Setup (Ollama version)

1. Install dependencies

pip install -r requirements.txt

2. Install and run Ollama

brew install ollama
ollama pull mistral
ollama serve

3. Run the app

source venv/bin/activate
streamlit run app.py

📸 Demo Screenshots

Homepage with input box
<img width="1265" alt="image" src="https://github.com/user-attachments/assets/db5a7e42-f7cf-47dd-89c6-a4cd54c02e5e" />


AI-generated interaction response
<img width="1153" alt="Screenshot 2025-05-01 at 7 17 57 AM" src="https://github.com/user-attachments/assets/d52b0a94-1b0e-4d6b-be1b-5557755d2d07" />


Terminal log of Mistral responding via Ollama

