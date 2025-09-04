
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask! 🎉"

if __name__ == "__main__":
    # Flaskサーバーを起動
    app.run(host="0.0.0.0", port=5000, debug=True)
