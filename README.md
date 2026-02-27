# RAG_Sagittarius_Fortune_Teller

**RAG_Sagittarius_Fortune_Teller** is a Retrieval-Augmented Generation (RAG) chatbot built with a Streamlit interface. It answers questions in the style of a mystical fortune teller using context retrieved from a local knowledge base.

## Features

- Streamlit web interface
- Retrieval-Augmented Generation (RAG) pipeline
- Local vector storage using FAISS
- Embeddings powered by HuggingFace models
- AI responses generated via Groq LLM
- Context-grounded answers (no hallucinated prophecies)

## Link to Streamlit App
- https://ragsagittariusfortuneteller.streamlit.app/

## How It Works

1. A text file (`horoscope.txt`) is loaded as the knowledge base.
2. The text is split into chunks using LangChain text splitters.
3. Chunks are converted into embeddings.
4. FAISS stores and retrieves the most relevant context.
5. Groq’s LLM generates a response using only the retrieved context.
6. The output is displayed in a clean Streamlit interface.

## Tech Stack

- **LangChain** – RAG pipeline orchestration  
- **FAISS** – Vector similarity search  
- **HuggingFace Embeddings** – Text vectorization  
- **Groq** – Large language model inference  
- **Streamlit** – Web interface  

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
