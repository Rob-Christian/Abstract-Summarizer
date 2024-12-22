# ArXiv Paper Abstract Summarizer
This project provides a simple web application to summarize abstracts of research papers from [arXiv](https://arxiv.org/). This app allows the user to input an ArXiv link, fetch the paper's metadata, and generate a summarized version of the paper's abstract using SOTA NLP.
# Model Information
The app uses the DistilBART model (sshleifer/distilbart-cnn-12-6) for text summarization. DistilBART is a smaller, faster version of the popular BART (Bidirectional and Auto-Regressive Transformers) model developed by Facebook AI. It is specifically designed for tasks like summarization and translation.
DistilBART reduces the size of the original BART model, making it significantly faster and less resource-intensive, while maintaining high-quality outputs. This model is ideal for real-time applications, where speed and accuracy are essential.
# How to Run the App?
Access the app through this [link](https://abstract-summarizer-0909.streamlit.app/)
# How can I redo this project?
1. Clone this repository to your local machine (the abstrac_summarizer.py and the requirements.txt file)
2. Sign-up in streamlit cloud, then use your repository to create the app.
