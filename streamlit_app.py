import streamlit as st
from retro_analyzer import analyze_feedback

st.title("🧠 Sprint Retrospective AI Analyzer")

input_text = st.text_area("Paste sprint feedback (one per line)", height=200)
if st.button("Analyze"):
    feedback_list = [line.strip() for line in input_text.split("\n") if line.strip()]
    results = analyze_feedback(feedback_list)
    for theme, texts in results.items():
        st.subheader(theme)
        for item in texts:
            st.write(f"- {item}")