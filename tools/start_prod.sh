#!/usr/bin/env bash
nohup tools/with_venv.sh gunicorn --reload -w 4 -b 0.0.0.0:80 server.app:app &