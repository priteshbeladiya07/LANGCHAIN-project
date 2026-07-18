# 🚀 LANGCHAIN Project

> A beginner-friendly collection of LangChain examples demonstrating different Chat Models and Embedding Models using Python.

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge)
![AI](https://img.shields.io/badge/Generative-AI-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

# 📌 About

This repository contains hands-on examples of **LangChain** concepts.

The project demonstrates:

- 🤖 Working with different LLM providers
- 💬 Building AI Chatbots
- 🔍 Using Embedding Models
- 🧠 HuggingFace Embeddings
- 📦 Modular Python Project Structure

This repository is ideal for beginners who are starting their journey in **Generative AI** and **LangChain**.

---

# 📂 Project Structure

```
LANGCHAIN_project/
│
├── MYBOT/
│   ├── UIMYbot.py
│   └── core.py
│
├── chatmodels/
│   ├── UIchatbot.py
│   ├── 1_chatmodel_groq.py
│   ├── 2_chatmodel_gemini.py
│   ├── 3_chatmodel_mistral.py
│   ├── chatbot.py
│   ├── UIChatbot.py
│   ├── huggingfacemodel.py
│   └──localmodel.py
│
├── embeddingmodels/
│   ├── embeddings.py
│   └── huggingface_embeddings.py
│
├── LLM/
│   └── demo.py
│
├── .gitignore
├── requirements.txt
└── README.md
│
├── requirements.txt
```

---

# 📁 Folder Explanation

## 📂 MYBOT/

Contains the core logic used by the chatbot.

| File | Description |
|------|-------------|
| **UIMYbot.py** | User Interface related core functionality |
| **core.py** | Main backend logic and reusable functions |

---

## 📂 chatmodels/

Examples of different Large Language Models supported by LangChain.

| File | Description |
|------|-------------|
| **UIchatbot.py** | Chatbot with a simple user interface |
| **1_chatmodel_groq.py** | Groq  integration |
| **2_chatmodel_gemini.py** | Google GeminiLLM integration |
| **3_chatmodel_mistral.py** | Mistral AI integration |
| **chatbot.py** | Basic chatbot implementation |

---

## 📂 embeddingmodels/

Examples of vector embedding models.

| File | Description |
|------|-------------|
| **embeddings.py** | Basic embedding model examples |
| **huggingface_embeddings.py** | HuggingFace embedding models using LangChain |

---

## 📄 requirements.txt

Contains all required Python libraries.

Install them using

```bash
pip install -r requirements.txt
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/jeetgondaliya2-prog/LANGCHAIN_project.git
```

Go inside the project

```bash
cd LANGCHAIN_project
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_API_KEY=your_api_key
GROQ_API_KEY=your_api_key
HF_TOKEN=your_huggingface_token
```

---

# ▶️ Running Examples

Run Gemini Chat Model

```bash
python chatmodels/chat_gemini_ai.py
```

Run Groq Model

```bash
python chatmodels/chat_groq_ai.py
```

Run Mistral Model

```bash
python chatmodels/chat_mistral_ai.py
```

Run Embedding Example

```bash
python embeddingmodels/embeddings.py
```

Run HuggingFace Embeddings

```bash
python embeddingmodels/huggingface_embeddings.py
```

---

# 📚 Technologies Used

- Python
- LangChain
- Google Gemini
- Groq
- Mistral AI
- HuggingFace
- dotenv

---

# 🎯 Learning Objectives

- Learn LangChain basics
- Understand Chat Models
- Explore Embedding Models
- Work with Multiple LLM Providers
- Build AI Chatbots
- Organize LangChain Projects

---

# 📖 Repository Contents

✅ Chat Models

- Gemini AI
- Groq AI
- Mistral AI

✅ Embedding Models

- LangChain Embeddings
- HuggingFace Embeddings

✅ Chatbot

- Basic Chatbot
- UI Chatbot

---

# 🤝 Contributions

Contributions are welcome!

Feel free to fork this repository and submit a pull request.

---

# 👨‍💻 Author

**Pritesh Beladiya**

- 🎓 IIIT Nagpur
- 💻 B.Tech ECE (2025–2029)
- 🌱 Learning Generative AI, Machine Learning & DSA

GitHub:
https://github.com/priteshbeladiya07

---

# ⭐ Support

If you found this repository helpful,

⭐ Star the repository

🍴 Fork it

📢 Share it with others

Happy Coding! 🚀
