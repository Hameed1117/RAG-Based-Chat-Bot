# 🧠 RAG-Based ChatBot (Local LLaMA 2 + Real-Time Web Search)

This project implements a **Retrieval-Augmented Generation (RAG)** chatbot using a local LLM and real-time web search integration — enabling factual, contextual, and up-to-date answers with zero dependency on OpenAI or remote inference.

## 🚀 What's Inside

| Component        | Description                                                              |
|------------------|--------------------------------------------------------------------------|
| 🧠 **LLaMA 2 7B Chat**   | Runs locally via `llama-cpp-python` using a quantized GGUF model      |
| 🔍 **Web Search**       | Integrated with `Serper.dev` (Google Search API) for real-time data   |
| 🧠 **RAG Loop**         | Combines retrieved snippets with prompt → sends to LLaMA               |
| 🧪 **Test Scripts**     | For validating local generation, search APIs, and full chat pipeline   |
| 💻 **Terminal Interface** | Interactive chat prompt with exit option for manual testing             |

---

## 🗂️ Project Structure

```text
📁 NLP-Rag Based Chat BOT/
├── llama_local.py         # Loads LLaMA 2 GGUF and defines inference
├── new_web_search.py      # Returns RAG-friendly formatted search results
├── serper_search.py       # Returns raw snippet list for testing/analysis
├── rag_chat.py            # Main chatbot: retrieval → generation
├── test_local_llama.py    # Test local LLaMA inference
├── test_serper.py         # Test raw Serper API response
├── test_rag.py            # Full RAG test (search + generate)
├── models/
│   └── llama-2-7b-chat.Q4_K_M.gguf
├── .env                   # Stores SERPER_API_KEY
├── .gitignore
├── README.md
├── requirements.txt
└── venv/                  # Python 3.10.10 virtual environment
````


## ⚙️ Setup Instructions

### 1. Create and Activate Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download LLaMA 2 GGUF Model

```bash
curl -L -o models/llama-2-7b-chat.Q4_K_M.gguf https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf
```

### 4. Set Your Serper API Key

Create a `.env` file:

```
SERPER_API_KEY=your_key_here
```

---

## 🧪 Run the Bot (Terminal Interface)

```bash
python rag_chat.py
```

Sample:

```
🧑 You: What’s the latest on AI safety?
🧠 Bot: [Answer generated using real-time search + LLaMA]
```

---

## ✅ Completed Milestones

* 🔁 Terminal chat loop
* 🌐 Web search integration (Serper)
* 🧠 Local LLaMA 2 model inference
* 📁 Modular project structure with test cases
* 📦 Ready for Phase 2: Flask API

---

## 🔜 Next Steps (Coming in `api-flask` branch)

| Feature                    | Status     |
| -------------------------- | ---------- |
| 🗂️ Flask API endpoints    | 🔜 Planned |
| 🖼️ Custom Web UI frontend | 🔜 Planned |
| 🌍 VPS / GitHub deployment | 🔜 Planned |

---

## 📌 Credits

* **Model**: Meta LLaMA 2 7B Chat
* **Quantization**: TheBloke (GGUF format)
* **Search API**: Serper.dev
* **Engine**: llama-cpp-python


Built with ❤️ by Khadhar Hameed Khan Pathan – a passionate AI engineer in the making.

````
