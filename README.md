# speech2text/app

Here we have the API implementation of the same in flask.

- **Language:** python
- **Path:** app/app.py

## RUNNING THE APP IN LOCAL SERVER

### 1. Environment Variables needded to run the app

Some environment variables are needed to run the app. Make sure you have them set.

- `export FLASK_APP=app.py`
- `export FLASK_ENV=development`

### 2. Running the app

It is as simple as (with given output)

    $ python run.py

     * Serving Flask app 'main.py' (lazy loading)

    - Serving Flask app 'app.main' (lazy loading)
    - Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    - Debug mode: off
    - Running on <http://127.0.0.1:5000> (Press CTRL+C to quit)
