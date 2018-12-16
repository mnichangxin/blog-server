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
    python3 -m env env
    . venv/bin/activate (Linux)
    venv\Scripts\activate (Windows)
```

* Install:

```sh
    pip(3) install -e .
```

* Configuration:

If `Linux`:

```sh
    export FLASK_APP=flaskr
    export FLASK_ENV=development
    flask run
```

If `Windows`:

```sh
    $env:FLASK_APP = "flaskr"
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