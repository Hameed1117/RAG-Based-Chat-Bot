from llama_cpp import Llama

# Load the local GGUF model
llm = Llama(
    model_path=r"C:\Programming\Natural Language Processing\NLP-Rag Based Chat BOT\models\llama-2-7b-chat.Q4_K_M.gguf",
    n_ctx=2048,
    verbose=False
)

# Function to query the model
def generate_local_llama_answer(prompt, max_tokens=300):
    full_prompt = f"[INST] {prompt} [/INST]"
    response = llm(full_prompt, max_tokens=max_tokens, stop=["</s>"])
    return response["choices"][0]["text"].strip()
