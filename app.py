
import streamlit as st
from rag_pipeline import get_interaction_explanation

st.set_page_config(page_title="Drug Interaction Checker", layout="centered")

st.title("💊 AI Drug Interaction Checker")
st.caption("Understand drug combinations in plain language — ethically and safely.")

query = st.text_input("🔎 Enter your query (e.g., Can I take ibuprofen with fluoxetine?)")

if st.button("Check Interaction"):
    if query:
        with st.spinner("Analyzing..."):
            response = get_interaction_explanation(query)
        st.markdown("### ✅ AI Response")
        st.write(response['answer'])
        st.markdown(f"*Sources: {', '.join(response['sources'])}*")
        st.warning("⚠️ This tool is for informational purposes only. Always consult your doctor.")
    else:
        st.error("Please enter a query to continue.")
