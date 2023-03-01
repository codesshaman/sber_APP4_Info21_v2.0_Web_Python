from flask_sqlalchemy import SQLAlchemy


def db_connect(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:'
    return SQLAlchemy(app)
