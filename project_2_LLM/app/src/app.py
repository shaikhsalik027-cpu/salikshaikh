import streamlit as st

st.set_page_config(
    page_title="Market Insights Assistant",
    page_icon="📈",
    layout="centered"
)

st.title("📈 Market Insights Assistant")
st.write(
    "Ask questions about the stock market, trends, or specific stocks."
)

user_input = st.text_input(
    "Ask a question:",
    placeholder="e.g. Analyze INFY stock"
)

if user_input:
    st.markdown("### 🤖 Response")
    st.write(
        "I’m alive ✅\n\n"
        "You asked: **{}**\n\n"
        "LLM integration coming next."
        .format(user_input)
    )