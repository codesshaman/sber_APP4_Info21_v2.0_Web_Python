import os

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres/[postgres]")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres/[postgres]'
SQLALCHEMY_TRACK_MODIFICATIONS = False