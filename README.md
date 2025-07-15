# OrgGuide-AI

**OrgGuide-AI** is a Multi-Agent AI application designed to streamline onboarding and internal support for organizations using an interactive, intelligent chatbot interface. Built with [Langflow](https://github.com/logspace-ai/langflow) and [Streamlit](https://streamlit.io/), it leverages RAG (Retrieval-Augmented Generation) agents, internal document parsing, and API-based access to company knowledge.

---

## 🧠 Features

- ✅ **Multi-Agent Support** using Langflow  
- ✅ **RAG (Retrieval-Augmented Generation)** for accurate and document-grounded answers  
- ✅ **Organization Chatbot Interface** for employee onboarding and internal help  
- ✅ **Streamlit UI** for simple web-based interaction  
- ✅ **Custom data ingestion** (CSV, text files, PDFs) for internal project and personnel lookup


## 🚀 Tech Stack

| Layer            | Tools/Frameworks                         |
|------------------|-------------------------------------------|
| AI Framework     | Langflow (built on LangChain)            |
| Frontend UI      | Streamlit                                |
| Backend API      | Langflow REST API                        |
| Document Parsing | RAG with CSVs, internal docs             |
| Deployment       | GitHub + Streamlit CLI (local dev)       |


## To Run
1. pip install -r requirements.txt

2. Create a .env file in the root directory with the following:
APP_TOKEN=your_langflow_application_token_here

3. streamlit run main.py

## Example Use Cases
“What is the NovaIQ project about?”
“Who is working on the CRM migration?”
“What tools does the Data team use?”
“How do I request PTO?”
“Who is the Director of Engineering?”
