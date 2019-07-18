# blog-server

Blog server, powered by python.

**Notes: All environments depend on `Python ^3.7`.**

## :package: Install

```sh
    tools/install.sh
```

## :hammer: Usage

```sh
    tools/start_dev.sh
```

## :memo: Introduction

[Flask](https://flask.palletsprojects.com/en/1.1.x/) is a lightweight WSGI web application framework. We are devolop micro-service based on `Flask`. The architecture of this micro-service is as follows： 

```

├── blog-server/
|   ├── server/
|       ├── __init__.py
|       ├── config/
|       |   └── __init__.py
|       ├── libs/
|       │   ├── __init__.py
|       │   ├── commands.py
|       │   ├── error.py
|       |   └── error_handler.py
|       ├── api/
|       │   ├── __init__.py
|       │   ├── view/
|       |   └── internal/
|       ├── service/
|       |   └── __init__.py
|       ├── dao/
|       |   └── __init__.py
|       ├── model/
|       |   └── __init__.py
|       └── utils/
|           └── __init__.py
├── tools/
├── venv/
├── .flaskenv
└── requirements.txt

```

## :wrench: Configuration

The file `.flaskenv` mark as `Flask` environmental variable.
