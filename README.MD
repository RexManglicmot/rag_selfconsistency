## Status  
![status](https://img.shields.io/badge/status-actively--developed-brightgreen)

This project is **currently** being developed and improved with additional features and testing.


## SubjectLine
**SubjectLine** is a production-grade AI retrieval-augmented generation (RAG) to recommend high-performing email subject lines based on real campaign data. It helps marketers uncover actionable insights grounded in metrics like open and click-through rates.

At the core of the system is a **self-consistency** mechanism, which generates multiple candidate answers to a query and selects the most stable, evidence-backed response. This reduces hallucinations and ensures that recommendations are accurate, repeatable, and trustworthy.

### Tech Stack  
Python · sentence-transformers · FAISS · transformers · Mistral-7B-Instruct · cosine similarity · Streamlit · logging · pytest · GitHub Actions · Docker


Project layout:
Set up venv, creat requirements and install, logger system, build out ingest_data.py etc., .env config, CI, tests, Docker