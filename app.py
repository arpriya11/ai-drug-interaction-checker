from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
from rag_pipeline_local import get_interaction_explanation_local as get_interaction_explanation
st.set_page_config(page_title="Drug Interaction Checker", layout="centered")

st.title("💊 AI Drug Interaction Checker")
st.caption("Understand drug combinations in plain language — ethically and safely.")

query = st.text_input("🔎 Enter your query (e.g., Can I take ibuprofen with fluoxetine?)")

if st.button("Check Interaction"):
    if query:
        print("🔁 Button clicked. Calling get_interaction_explanation()...") 
        with st.spinner("Analyzing..."):
            try:
                response = get_interaction_explanation(query)
                print("✅ Response received:", response)
                st.markdown("### ✅ AI Response")
                st.write(response['answer'])
                st.markdown(f"*Sources: {', '.join(response['sources'])}*")
            except Exception as e:
                st.error(f"❌ Error occurred: {e}")
                import traceback
                st.text(traceback.format_exc())
        st.warning("⚠️ This tool is for informational purposes only. Always consult your doctor.")
    else:
        st.error("Please enter a query to continue.")
