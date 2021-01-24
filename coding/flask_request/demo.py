from flask import Flask, request


app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello():
    params = request.args
    print params
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)
