from controllers.all_path import above_directory
from flask import Flask, url_for
from controllers.routes import app_route


app = Flask(__name__)
# app.config.from_pyfile("config.py")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@postgres:5432/postgres'
# connect.init_app(app)
app.register_blueprint(app_route)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
