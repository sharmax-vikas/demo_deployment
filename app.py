import streamlit as st
import os
import sys
# PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(PROJECT_ROOT)
from load_model import sent


def main():
    st.title("Sentiment Analysis App")

    # Text input
    text = st.text_area("Enter your text query:", height=100)

    # Submit button
    if st.button("Submit"):
        # Tokenize input text
        res = sent(text)
        st.write("Sentiment Analysis Results:")
        st.write(f"Sentiment: {'Positive' if res == 1 else 'Negative'}")


if __name__ == "__main__":
    main()

