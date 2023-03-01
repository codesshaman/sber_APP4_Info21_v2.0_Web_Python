from flask import Flask, url_for
from controllers.routes import app_route
from controllers.db_connection import db_connect

app = Flask(__name__)
app.register_blueprint(app_route)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
