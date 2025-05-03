from web_search import search_web
from llama_local import generate_local_llama_answer

def rag_answer(question):
    search_context = search_web(question)
    if not search_context or "[ERROR]" in search_context:
        return "🔍 This is beyond my current knowledge. I will try to help you in the future."

    prompt = (
        f"You are an expert assistant. Using the information below from a web search, answer the user's question.\n\n"
        f"Web Search Results:\n{search_context}\n\n"
        f"Question: {question}\nAnswer:"
    )

    return generate_local_llama_answer(prompt)

# Add at the end of rag_chat.py
if __name__ == "__main__":
    while True:
        user_q = input("\n🧑 You: ")
        if user_q.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        response = rag_answer(user_q)
        print("\n🤖 Bot:", response)
