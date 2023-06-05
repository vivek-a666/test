import streamlit as st
from textblob import TextBlob
import nltk

nltk.download('punkt')

def main():
    st.title("Token Healer")
    
    # Input text
    text = st.text_area("Enter text:")
    
    # Process the text when the user clicks the "Correct" button
    if st.button("Correct"):
        blob = TextBlob(text)
        corrected_text = ""
        
        for token in blob.tokens:
            if token.isalpha():
                corrected_word = token.correct()
                corrected_text += str(corrected_word) + " "
            else:
                corrected_text += str(token) + " "
        
        # Display the corrected text
        st.text("Corrected Text:")
        st.write(corrected_text)

if __name__ == "__main__":
    main()
