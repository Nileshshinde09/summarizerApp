import streamlit as st

def about_section():
    st.title("About This NLP Application")
    st.write(
        "Welcome to our Natural Language Processing (NLP) application! This app is designed to help you analyze and process text data using the TF-IDF vectorizer algorithm."
    )

    st.subheader("What is TF-IDF?")
    st.write(
        "TF-IDF (Term Frequency-Inverse Document Frequency) is a widely used NLP algorithm that helps in text analysis and information retrieval. It quantifies the importance of a term within a document relative to a collection of documents (corpus). The higher the TF-IDF score of a term in a document, the more important or relevant it is to that document."
    )

    st.subheader("Key Features of this App:")
    st.write(
        "1. **Text Summarization:** You can use the app to summarize longer texts, making it easier to understand the main points of a document or article."
    )
    st.write(
        "2. **Keyword Extraction:** Discover important keywords within your text, which can be valuable for SEO or content analysis."
    )
    st.write(
        "3. **TF-IDF Analysis:** Perform TF-IDF analysis to determine the importance of words within a document or a corpus of documents."
    )

    st.subheader("How to Use the App:")
    st.write(
        "1. In the sidebar, you'll find navigation links to different sections of the app, including 'Home' (where you are now), 'About,' 'Text Summarization,' and 'TF-IDF Analysis.'"
    )
    st.write(
        "2. To access a specific feature, click on the corresponding link in the sidebar, and the main content area will update with the relevant functionality."
    )
    st.write(
        "3. Feel free to experiment with different text inputs, adjust settings, and explore the capabilities of this NLP application."
    )

    st.subheader("Acknowledgments")
    st.write(
        "This app is powered by Python and Streamlit. We also use the TF-IDF vectorizer algorithm for text analysis."
    )

# Create an "About" section in the Streamlit app
if __name__ == "__main__":
    about_section()
