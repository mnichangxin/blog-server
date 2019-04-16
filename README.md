# vue-blog-server

The personal website server.

**Notes: All environments depend on `Python ^3.7`.**

## V0.0.1 Flask

* Flask project demo layout: 

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

* Create virtual environment:

```sh
    python3 -m venv venv
    #OR (Windows)
    py -3 -m venv venv
```

* Active virtual environment:

```sh
    . venv/bin/activate
    #OR (Windows)
    venv\Scripts\activate
```

* Install:

```sh
    pip3 install -r requirements.txt
```

* Configuration:

```sh
    [export FLASK_APP=app]
    [export FLASK_ENV=development]
    #OR (Windows)
    [$env:FLASK_APP = "app"]
    [$env:FLASK_ENV = "development"]
```

* Run start:

```sh
    flask run
```

Finally start at default `http://127.0.0.1:5000/`.