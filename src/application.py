from flask import Flask, Response, request

app = Flask(__name__)


@app.route("/", methods=["GET", "HEAD"])
def index():
    if request.method == "HEAD":
        return Response(status=200)

    return "This is response from server!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
