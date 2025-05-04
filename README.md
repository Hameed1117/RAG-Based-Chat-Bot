# 🧠 RAG-Based ChatBot – Second Phase (Flask UI + Local LLaMA)

This is the **second-phase branch** of my RAG (Retrieval-Augmented Generation) ChatBot project. In this phase, I moved from a terminal-only prototype to a full-stack web app using **Flask**, while still keeping everything local using Meta’s LLaMA 2 7B Chat model.

---

## ✅ What I’ve Done So Far

### 🧠 Local Model Inference

* Using **Meta's LLaMA 2 7B Chat (GGUF)** model locally
* Loaded the quantized `.gguf` model with `llama-cpp-python`
* Created a reusable function to generate answers from prompts

### 🌐 Web Search with Serper.dev

* Integrated **Serper.dev** to fetch real-time Google search results
* Modularized logic inside `serper_search.py`
* Merged results with prompt templates to guide LLaMA's generation

### 💻 Flask Backend

* Created a RESTful API using **Flask**
* `/ask` endpoint accepts POST requests with a question
* Response is generated using LLaMA + Serper search
* Kept debug off and multi-threading enabled for smooth local testing

### 💬 Basic Web UI (Phase 1)

* Built a simple but neat web UI using HTML, CSS, and JS
* Chat interface mimics real conversation
* Removed background animations to save compute
* Optimized user input behavior and auto-scroll chat history

### 🧹 Project Clean-up

* `.gitignore` filters out `.env`, `venv/`, and `.gguf` model files
* `requirements.txt` updated to include Flask and other packages
* Folder structure organized for clarity

---

## 📁 Current Project Structure

```bash
├── app.py                 # Flask backend
├── rag_chat.py            # RAG logic (search + prompt + LLM)
├── llama_local.py         # Local LLaMA model inference
├── serper_search.py       # Web search API logic
├── templates/
│   └── index.html         # Web chat layout
├── static/
│   └── style.css          # Chat UI design
├── .env                   # Stores SERPER_API_KEY (excluded from Git)
├── .gitignore             # Excludes venv, env vars, model files
├── requirements.txt       # All Python dependencies
```

---

## 🚧 Future Updates

| Feature                             | Status     |
| ----------------------------------- | ---------- |
| 🌐 Replace local LLaMA with LLM API | 🔜 Planned |
| 🚀 Deploy on Render or Railway      | 🔜 Planned |
| 💾 Add conversation logging         | 🔜 Later   |
| ✨ Enhance UI with dynamic effects   | 🔜 Later   |

---

## 👤 About Me

Built by **Khadhar Hameed Khan Pathan**, a master's student passionate about applied NLP and full-stack AI products.

> "From scratch to smart — building my own ChatGPT with RAG + LLaMA from the ground up."

---

🔁 Stay tuned for API integration and full cloud deployment in the next phase!
