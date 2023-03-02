import os

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgres://postgres@postgres:5432/postgres")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres/[postgres]'
SQLALCHEMY_TRACK_MODIFICATIONS = False