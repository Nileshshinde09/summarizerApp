import streamlit as st
from summeriser import summerize
def runhome():
    text = st.text_area("Enter your text here:")


    # Summarization button
    if st.button("Summarize"):
        if len(text)>100:
            summarized_text = summerize(text)
            st.subheader("Summarized Text:")
            st.write(summarized_text)
        elif text=='':
            st.warning("Please enter some text for summarization.")
        else:
            st.warning("Your entered text is not enough to make summary, Enter more text.")

    st.success("Developed by Nilesh Shinde")