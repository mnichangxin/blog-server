#!/usr/bin/env bash
VENV_DIRNAME="venv" 
if [ ! -d $VENV_DIRNAME ]
then
    # python3 -m venv $VENV_DIRNAME
    virtualenv venv
fi
source $VENV_DIRNAME/bin/activate && "$@"