# vue-blog-server

The personal website server.

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

* Run start: 

If Linux:

```sh
    export FLASK_APP=flaskr
    export FLASK_ENV=development
    flask run
```

If Windows:

```sh
    $env:FLASK_APP = "flaskr"
    $env:FLASK_ENV = "development"
    flask run
```

Then start at default `http://127.0.0.1:5000/`.