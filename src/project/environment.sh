#!/bin/bash
if [ ! -d "venv" ]; then
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
fi
if [ ! -f "requirements.txt" ]; then
    touch requirements.txt
    pip install Flask
    pip install flake8
    pip instal psycopg2-binary
    pip freeze >> requirements.txt
    pip install --upgrade pip
  else
    pip install -r requirements.txt
    pip freeze
fi
echo "For switch to environment use command: "
echo "source venv/bin/activate"
