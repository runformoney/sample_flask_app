import argparse
from flask import Flask, render_template, request, jsonify
from src import db_helper_postgres

app = Flask(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Flask App Arguments")
    parser.add_argument(
        "--host", type=str, default="127.0.0.1", help="Host address to bind to"
    )
    parser.add_argument(
        "--port", type=int, default=8091, help="Port number to listen on"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    app.run(debug=True, host=args.host, port=args.port)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/show_user_page", methods=["GET"])
def show_user_data():
    return render_template("show_user.html")


@app.route("/show_user", methods=["GET"])
def show_user():
    data = db_helper_postgres.get_all_students()
    return jsonify(data)


@app.route("/insert_user", methods=["POST"])
def insert_user():
    user_name = request.form.to_dict().get("name").title()
    roll_number = db_helper_postgres.insert_user(user_name)
    return {"message": f"{user_name} was assigned Roll Number: {roll_number}"}


@app.route("/insert_user_page", methods=["GET"])
def insert_user_page():
    return render_template("insert_user.html")


if __name__ == "__main__":
    main()
