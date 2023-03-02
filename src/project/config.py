import os

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgres://http://postgres:5432")
SQLALCHEMY_TRACK_MODIFICATIONS = False