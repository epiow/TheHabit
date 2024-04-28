#!/bin/sh
if [[ "$VIRTUAL_ENV" != "" ]]
then
    python3 -m venv .venv &
    source .venv/bin/activate &
    pip3 install -r requirements.txt
fi