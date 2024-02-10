from flask import Flask, render_template, request, jsonify
from src import db_helper_postgres

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/show_user", methods=["POST"])
def show_user():
    data = db_helper_postgres.select_all_from_class_table()
    return jsonify(data)
    # return jsonify(
    #     {
    #         "data": [
    #             {"name": "Ifra Irshin ", "roll_number": 1},
    #             {"name": "Hifzur Rahman ", "roll_number": 2},
    #         ]
    #     }
    # )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8091)
