from flask import Flask, url_for
from controllers.routes import app_route
from model import journal
# import logging


# level = journal.debug_level()
# logging.basicConfig(level=level, filename="logs/log_.log",
#                     format="%(levelname)s %(asctime)s %(module)s %(name)s %(message)s")

app = Flask(__name__)
# connect.init_app(app)
app.register_blueprint(app_route)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

    # app.run(debug=True, host='0.0.0.0')
