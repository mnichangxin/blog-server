#!/usr/bin/env bash
VENV_DIRNAME="venv" 
if [ ! -d $VENV_DIRNAME ]
then
    virtualenv venv
fi
source $VENV_DIRNAME/bin/activate && "$@"