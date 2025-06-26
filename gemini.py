from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Replace with your actual Gemini API key
GEMINI_API_KEY = "AIzaSyDlqbKM4BIsvukkGZ04YHxhLLag5rZFavo"

@app.route("/api/gemini", methods=["POST"])
def gemini_proxy():
    data = request.json
    prompt = data.get("prompt", "")

    gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }
      try:
        response = requests.post(gemini_url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        text = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No content returned.")
        return jsonify({"result": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5001)
'''

with open("/mnt/data/gemini.py", "w") as f:
    f.write(gemini_py_code)
