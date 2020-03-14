# blog-server

Blog server, powered by python.

**Notes: All environments depend on `Python ^3.7`.**

## :package: Install

```sh
    tools/install.sh
```

## :hammer: Usage

* Dev:

```sh
    tools/start_dev.sh
```

* Prod:

```sh
    tools/start_prod.sh
```

## :memo: Introduction

[Flask](https://flask.palletsprojects.com/en/1.1.x/) is a lightweight WSGI web application framework. We are devolop micro-service based on `Flask`. The architecture of this micro-service is as follows： 

```

├── blog-server/
|   ├── server/
|       ├── __init__.py
|       ├── config/
|       ├── libs/
|       │   ├── commands.py
|       │   ├── error.py
|       |   └── error_handler.py
|       ├── api/
|       │   ├── view/
|       |   └── internal/
|       ├── service/
|       |   └── post.py
|       ├── dao/
|       ├── model/
|       └── utils/
├── tools/
├── venv/
├── .flaskenv
└── requirements.txt

```

## :wrench: Configuration

The file `.flaskenv` mark as `Flask` environmental variable.

## :pencil: Doc

The following API:

* [End-B](https://github.com/mnichangxin/blog-server/blob/dev-flask/doc/api-b.md)
* [End-C](https://github.com/mnichangxin/blog-server/blob/dev-flask/doc/api-c.md)