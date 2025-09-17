import streamlit as st
from Translator import prompt,llm

st.set_page_config(page_title="AI Translator",page_icon="🌍",layout="centered")

st.title("🌍 AI-Powered Language Translator")
st.write("Translate any word, phrase, or sentence into clear, simple English.")

#Input Box
user_input=st.text_area("✍️ Enter text to translate:", placeholder="Type here...")

if st.button("Translate"):
    if user_input.strip():
        with st.spinner("Traslatating...⏳"):
            formatted_prompt= prompt.format(word=user_input)
            response = llm.invoke(formatted_prompt)
            st.success("✅ Translation Complete!")
            st.markdown("### 🔎 Translation Result:")
            st.info(response.content)
    
    else:
        st.warning("⚠️ Please enter some text before clicking Translate.")


st.markdown("---")
st.markdown("💡 Powered by **Google Generative AI** & LangChain | Built with ❤️ using Streamlit")