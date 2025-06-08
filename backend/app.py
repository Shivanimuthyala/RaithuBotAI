# backend/app.py
from flask import Flask, request, jsonify, send_file
import joblib
from googletrans import Translator
from gtts import gTTS
import os
from flask_cors import CORS
from io import BytesIO

app = Flask(__name__)
CORS(app)

model = joblib.load(os.path.join("..", "model", "model.pkl"))
translator = Translator()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    query = data.get("query")
    lang = data.get("lang", "en")

    if not query:
        return jsonify({"response": "No query received."}), 400

    if lang == "te":
        query = translator.translate(query, src='te', dest='en').text

    response = model.predict([query])[0]

    if lang == "te":
        translated_response = translator.translate(response, src='en', dest='te').text
    else:
        translated_response = response

    return jsonify({"response": translated_response})

@app.route("/tts", methods=["POST"])
def tts():
    data = request.json
    text = data.get("text")
    lang = data.get("lang", "en")

    if not text:
        return "No text provided", 400

    tts = gTTS(text=text, lang='te' if lang == 'te' else 'en')
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return send_file(fp, mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(debug=True)
