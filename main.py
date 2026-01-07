from flask import Flask , request , render_template,jsonify
from google import genai

client = genai.Client(api_key="AIzaSyD2IgKYk-fce9NePQpctlSwVKWIVsncxrw")
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/chat" , methods=["POST"])
def chat():
    prompt = request.json["message"]
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt 
    )
    return jsonify({"reply": response.text})

app.run(port=8000)

