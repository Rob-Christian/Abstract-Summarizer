# import necessary libraries
import streamlit as st
import arxiv
import transformers
from transformers import pipeline

# Use BART model by Facebook for text summarization task
#summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Title of the streamlit app
st.title("ArXiv Paper Abstract Summarizer")

# Description
st.write(
    """
    **Welcome to the ArXiv Paper Abstract Summarizer!**
    
    This application allows you to quickly summarize the abstracts of research papers hosted on [arXiv](https://arxiv.org/). 
    By entering an arXiv paper URL, you can extract its abstract and receive a concise summary using a state-of-the-art (SOTA)
    natural language processing (NLP) model. 

    ---
    
    ### About the Model
    This app uses the [BART (Bidirectional and Auto-Regressive Transformers)](https://arxiv.org/abs/1910.13461) 
    summarization model, specifically `facebook/bart-large-cnn`. BART is a powerful transformer-based architecture 
    that has been pretrained on large datasets for tasks like summarization and translation. No fine-tuning has been 
    performed for this specific application, so results may vary depending on the content of the abstract.

    ---
    
    ### Disclaimer
    - This tool provides summaries based solely on the paper abstract, not the full content of the paper.
    - Summaries are generated using a pretrained model without additional fine-tuning. They may not always accurately 
      capture the full context or technical nuances.
    - Always refer to the original abstract and full paper for detailed understanding and accurate interpretation.
    """
)

# Request an input from the user
arxiv_url = st.text_input("Enter an ArXiv Paper URL")

if arxiv_url:
    try:
        # Extract the arXiv ID from the URL
        arxiv_id = arxiv_url.split("/")[-1]
        
        # Search for the paper using the arXiv ID
        search = arxiv.Search(id_list=[arxiv_id])
        paper = next(search.results(), None)
        
        if paper:
            st.write("## Paper Details")
            st.write(f"**Title**: {paper.title}")
            st.write(f"**Authors**: {', '.join(author.name for author in paper.authors)}")
            st.write(f"**Published Date**: {paper.published.date()}")
            
            st.write("### Original Abstract")
            st.write(paper.summary)
            
            # Summarize the abstract
 #           st.write("### Summarized Abstract")
 #           summarized_text = summarizer(paper.summary, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
 #           st.write(summarized_text)
        else:
            st.error("No paper found with the provided URL.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please enter a valid arXiv paper URL.")
