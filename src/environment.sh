#!/bin/bash
if [ ! -d "venv" ]; then
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
fi
if [ ! -f "requirements.txt" ]; then
    touch requirements.txt
    pip install Flask
    pip freeze >> requirements.txt
    pip install --upgrade pip
  else
    pip install -r requirements.txt
    pip freeze
fi
source venv/bin/activate
