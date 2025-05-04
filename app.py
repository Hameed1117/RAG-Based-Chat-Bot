from flask import Flask, request, jsonify, render_template
from rag_chat import rag_answer

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    if not data or "question" not in data:
        return jsonify({"error": "Missing 'question'"}), 400

    question = data["question"].strip()
    if not question:
        return jsonify({"error": "Empty question"}), 400

    try:
        response = rag_answer(question)
        return jsonify({"question": question, "answer": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False, threaded=True)
