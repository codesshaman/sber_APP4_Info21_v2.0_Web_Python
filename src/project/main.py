from controllers.all_path import above_directory
from flask import Flask, url_for
from controllers.routes import app_route

app = Flask(__name__)
# connect.init_app(app)
app.register_blueprint(app_route)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run(debug=True, host='0.0.0.0')
