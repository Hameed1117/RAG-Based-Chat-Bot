# test_rag.py
from rag_chat import rag_answer

if __name__ == "__main__":
    question = "What are the recent breakthroughs in AI safety?"
    print("Question:", question)
    print("\nAnswer:\n", rag_answer(question))
