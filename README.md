# blog-server

Blog server, powered by python.

**Notes: All environments depend on `Python ^3.7`.**

## V1.0.0 Flask

* Flask project demo layout: 

```

├── vue-blog-server/
|   ├── app/
|       ├── __init__.py
|       ├── commands.py
|       ├── config.py
|       ├── api/
|       │   ├── __init__.py
|       │   ├── blog/
|       |   └── admin/
|       └── db/
|           ├── __init__.py
|           └── models.py
├── venv/
├── .flaskenv
├── MANIFEST.in
└── requirements.txt

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