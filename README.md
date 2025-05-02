**Offline AI Drug Interaction Checker**

This project is a fully offline AI-powered app that helps non-experts understand drug interactions in simple, plain language. Built using Streamlit and Ollama with the Mistral 7B model, this assistant is designed to be accessible, privacy-friendly, and safe — no internet connection required.



**Problem**

Most drug interaction checkers require an internet connection and present information in clinical or confusing terms. This tool aims to:

Simplify medication safety information

Make it accessible to laypersons

Ensure offline access for better privacy and control



 **Goals**

Understand if medications may interact

Generate clear, simplified language

Include appropriate safety warnings and disclaimers

Work entirely on local hardware without any cloud dependency



**Key Features**

Runs fully offline using Ollama + Mistral 7B
Simple language responses optimized for non-experts
Ethical safety guardrails (no dosage, always disclaimers)
Fast, responsive UI with Streamlit



**Architecture Overview**

User Input (Streamlit UI)
        ↓
Prompt Template Applied (in Python)
        ↓
Local LLM Inference via Ollama (Mistral model)
        ↓
Response + Disclaimer shown in UI

**Example Query**
User: Can I take ibuprofen with fluoxetine?AI: “Ibuprofen and fluoxetine taken together may increase the risk of stomach bleeding. Always consult your doctor before combining these medications.”

** Stack

LLM: Mistral 7B

Inference Engine: Ollama

UI: Streamlit

Language: Python**


**Folder Structure**

drug-interaction-checker/
├── app.py                   # Streamlit app (offline)
├── rag_pipeline_local.py    # Model logic and prompt
├── requirements.txt         # Dependencies


 **Setup Instructions**

1. Clone the repo & set up a virtual environment

git clone https://github.com/YOUR_USERNAME/drug-interaction-checker.git
cd drug-interaction-checker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

2. Install and run Ollama

brew install ollama   # macOS only
ollama pull mistral
ollama serve          # Keep this running in a separate terminal

3. Run the app

streamlit run app.py

Then open http://localhost:8501 in your browser.

**Evaluation Strategy**


Relevance: Manual validation against trusted sources

Safety: No hallucinated dosage advice, disclaimers enforced

**Limitations**

Not intended for emergency use

Drug info is not real-time synced with medical databases

For educational/demo use only

🔮 Future Plans

Add offline vector DB of FDA + MedlinePlus

Voice command integration

Multi-language support

Android/iOS wrapper for mobile use

🙌 Acknowledgments

Ollama for offline LLMs

Streamlit for UI

Mistral AI for open-weight models

**🔧 Local Setup (Ollama version)**

1. Install dependencies

pip install -r requirements.txt

2. Install and run Ollama

brew install ollama
ollama pull mistral
ollama serve

3. Run the app

source venv/bin/activate
streamlit run app.py

**📸 Screenshots**

Homepage with input box
<img width="1265" alt="image" src="https://github.com/user-attachments/assets/db5a7e42-f7cf-47dd-89c6-a4cd54c02e5e" />


AI-generated interaction response
<img width="1153" alt="Screenshot 2025-05-01 at 7 17 57 AM" src="https://github.com/user-attachments/assets/d52b0a94-1b0e-4d6b-be1b-5557755d2d07" />




