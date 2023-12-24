# Flask SQLite Example

This is a simple Flask app that demonstrates how to create a web application with SQLite database integration. The app allows users to add their first name and last name, which gets stored in an SQLite database.

## Prerequisites

- Python 3.x installed on your machine.
- [Git](https://git-scm.com/) installed.
- [Docker](https://www.docker.com/) installed.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/flask-sqlite-example.git
    ```

2. Navigate to the project directory:

    ```bash
    cd flask-sqlite-example
    ```

## Run the Flask App Locally

3. (Optional) Create a virtual environment:

    ```bash
    python -m venv venv
    ```

    Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the Flask app:

    ```bash
    python app.py
    ```

    The app will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

## Create a Docker Image

6. Create a Docker image:

    ```bash
    docker build -t flask-sqlite-example .
    ```

7. Run the Docker container:

    ```bash
    docker run -p 5000:5000 flask-sqlite-example
    ```

    The app will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

## View SQLite Database

8. (Optional) Install [DB Browser for SQLite](https://sqlitebrowser.org/).

9. Open `database.db` in the `src` directory using DB Browser for SQLite to visualize the data.

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
