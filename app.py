import argparse
from flask import Flask, render_template, request, jsonify
from src import db_helper_postgres

app = Flask(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Flask App Arguments")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host address to bind to")
    parser.add_argument("--port", type=int, default=8091, help="Port number to listen on")
    return parser.parse_args()


def main():
    args = parse_args()

    # Use args.host and args.port in the app.run() method
    app.run(debug=True, host=args.host, port=args.port)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/show_user", methods=["POST"])
def show_user():
    data = db_helper_postgres.select_all_from_class_table()
    return jsonify(data)


if __name__ == "__main__":
    main()
