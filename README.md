# Flask SQLite Example

This is a simple Flask app that demonstrates how to create a web application with SQLite database integration. The app allows users to add their first name and last name, which gets stored in an SQLite database.

## Prerequisites

- Python 3.x installed on your machine.
- [Git](https://git-scm.com/) installed.
- (Optional) [DB Browser for SQLite](https://sqlitebrowser.org/) to visualize the SQLite database.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/flask-sqlite-example.git
    ```

2. Navigate to the project directory:

    ```bash
    cd flask-sqlite-example
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Run the Flask App

6. Run the Flask app:

    ```bash
    python app.py
    ```

    The app will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

## View SQLite Database

7. (Optional) Install [DB Browser for SQLite](https://sqlitebrowser.org/).

8. Open `database.db` in the `src` directory using DB Browser for SQLite to visualize the data.

## Project Structure

- `src`: Contains the Flask application code.
  - `__pycache__`: Auto-generated directory for Python bytecode.
- `static`: Contains static files (CSS, images, scripts).
  - `images`: Place for your images.
  - `scripts`: JavaScript files.
  - `style`: CSS files.
- `templates`: HTML templates for the Flask app.

Feel free to explore and modify the code to understand how the Flask app works. If you have any questions or run into issues, don't hesitate to ask.

Happy coding!
