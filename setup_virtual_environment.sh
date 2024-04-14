#!/bin/sh
if [[ "$VIRTUAL_ENV" != "" ]]
then
    exec python3 -m venv .venv
    exec source .venv/bin/activate
    exec pip3 install -r requirements.txt.
fi