#!/usr/bin/env bash
if [[ -n $1 && $1 == "--drop" ]]
then
    tools/with_venv.sh flask initdb --drop
else
    tools/with_venv.sh flask initdb
fi