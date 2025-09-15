from flask import Flask

TEAM_NAME = "Bony Tech"

app = Flask(__name__)

@app.route("/")
def home():
    return f"<h1>Welcome to {TEAM_NAME} Webpage 🚀</h1><p>This is running on Flask in OpenShift.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
