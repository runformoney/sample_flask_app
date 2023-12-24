from flask import Flask, render_template, request, jsonify
from src import db_helper

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_user', methods=['POST'])
def add_user():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    response = db_helper.add_data_to_db(first_name, last_name)
    if response:
        return jsonify({'message': 'User added successfully'})
    else:
        return jsonify({'message': 'Issue adding user to DB'})


if __name__ == '__main__':
    db_helper.create_table()
    app.run(debug=True)
