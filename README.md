# vue-blog-server

The personal website server.

**Notes: All environments depend on `Python ^3.7`.**

## V0.0.1 Flask

* Project layout: 

```

├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in

```

* Create virtual environment and activate:

```sh
    python3 -m env env (Linux)
    py -3 -m env env (Windows)
    . venv/bin/activate (Linux)
    venv\Scripts\activate (Windows)
```

* Install:

```sh
    pip3 install -r requirements.txt
```

* Configuration:

If `Linux`:

```sh
    export FLASK_APP=app
    export FLASK_ENV=development
    flask run
```

If `Windows`:

```sh
    $env:FLASK_APP = "app"
    $env:FLASK_ENV = "development"
    flask run
```

* Init DateBase:

```sh
    flask init-db
```

* Run start:

```sh
    flask run
```

Finally start at default `http://127.0.0.1:5000/`.