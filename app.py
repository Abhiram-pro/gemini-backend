from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "OK", "message": "Gemini backend is live"})

@app.route("/ask", methods=["GET", "POST"])
def ask():
    user_prompt = request.args.get("prompt") if request.method == "GET" else request.json.get("prompt")
    
    if not user_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_prompt)
    reply_text = response.text

    return jsonify({"reply": reply_text})

if __name__ == "__main__":
    app.run(debug=True)
