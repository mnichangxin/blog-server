#!/usr/bin/env bash
tools/with_venv.sh gunicorn --reload -w 4 -b 0.0.0.0:5000 server:app