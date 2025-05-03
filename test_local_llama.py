from llama_local import generate_local_llama_answer

question = "What is quantum entanglement in simple terms?"
answer = generate_local_llama_answer(question)

print("\n🧠 Local LLaMA 2 Response:\n")
print(answer)
