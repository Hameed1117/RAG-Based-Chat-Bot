# 🧠 RAG-Based ChatBot (Local LLaMA 2 + Web Search)

This project implements a **Retrieval-Augmented Generation (RAG)** chatbot powered by:

- 🔍 **Real-time web search** using [Serper.dev (Google Search API)](https://serper.dev)
- 🧠 **Local inference** using **Meta’s LLaMA 2 7B Chat** model (GGUF format)
- ✅ Fully **offline generation**, no token limits, no OpenAI dependence
- 📦 Packaged in a clean Python setup with a virtual environment

---

## 📁 Project Structure

| File/Folder              | Purpose |
|--------------------------|---------|
| `llama_local.py`         | Loads the local LLaMA 2 GGUF model and defines the inference function |
| `test_local_llama.py`    | Test script to verify LLaMA 2 responds correctly to a static prompt |
| `web_search.py`          | Connects to Serper.dev to fetch real-time search results |
| `rag_chat.py`            | Main chatbot logic: searches → builds prompt → gets LLaMA reply |
| `models/`                | Stores the downloaded GGUF model (`llama-2-7b-chat.Q4_K_M.gguf`) |
| `venv/`                  | Python 3.10.10 virtual environment |
| `.env` (optional)        | Store `SERPER_API_KEY` here if desired (currently hardcoded) |

---

## ✅ What We've Done So Far

1. 🔧 Created Python 3.10.10 virtual environment
2. 💡 Chose **LLaMA 2 7B Chat** as our base model for generation
3. 🔽 Downloaded quantized `GGUF` model from Hugging Face (TheBloke)
4. 🚀 Loaded it using `llama-cpp-python` for fast local inference
5. 🌐 Integrated Serper API to fetch Google search snippets
6. 🔄 Built a full **RAG loop** combining retrieval + generation
7. 🧪 Successfully tested real-world queries (e.g., current date, events, ML definitions)

---

## ⚙️ Setup Instructions

### 1. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
````

### 2. Install Dependencies

```bash
pip install llama-cpp-python requests
```

### 3. Download LLaMA 2 Model (GGUF)

Use real curl:

```bash
curl -L -o models/llama-2-7b-chat.Q4_K_M.gguf https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf
```

### 4. Add Your Serper API Key

Edit `web_search.py` and set your key:

```python
SERPER_API_KEY = "your_real_key"
```

---

## 🧪 Run the Bot

```bash
python rag_chat.py
```

Type your question. Example:

```
what is today's date and what events are happening this week?
```

---

## 🚧 Future Improvements

| Feature                                 | Status      |
| --------------------------------------- | ----------- |
| 🔁 Terminal chat loop                   | ✅ Done      |
| 🌐 Web search (Serper) integration      | ✅ Done      |
| 🧠 Local model inference                | ✅ Done      |
| 🗂️ Convert to modular Flask API        | 🔜 Next     |
| 🖼️ Add custom web UI                   | 🔜 Planned  |
| 🌍 Deploy to GitHub + personal VPS      | 🔜 Planned  |
| 🧪 Add RAG benchmarking + eval          | 🔜 Optional |
| ✍️ Prompt refinement / context chunking | 🔜 Future   |

---

## 📌 License & Credits

* Model: [Meta LLaMA 2 7B Chat](https://ai.meta.com/llama/)
* GGUF: [TheBloke on Hugging Face](https://huggingface.co/TheBloke)
* Web Search: [Serper.dev](https://serper.dev)
* Engine: [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)

---

Built with ❤️ by a passionate AI engineer in the making.

```

---

Would you like me to package this in a file or also generate a `requirements.txt` and `.gitignore` to go with it?
```
