from flask import Flask, request, jsonify, make_response
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure Gemini API
genai.configure(credentials="bamboo-striker-299906-b9fa76a9324e.json")

@app.route("/ask", methods=["POST"])
def ask_gemini():
    user_prompt = request.json.get("prompt", "")
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_prompt)
        reply = response.text

        # Force proper JSON response
        return make_response(jsonify({"reply": reply}), 200)
    except Exception as e:
        return make_response(jsonify({"error": str(e)}), 500)

if __name__ == "__main__":
    app.run(debug=True)
