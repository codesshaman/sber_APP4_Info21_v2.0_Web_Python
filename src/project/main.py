from controllers.routes import app_route
from flask import Flask
from datetime import datetime
from model import journal
from loguru import logger
import logging

level = journal.debug_level()

date_time = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

logfile_name = "logs/log_" + date_time


def create_app():
    my_app = Flask(__name__)
    my_app.secret_key = "some_secret"
    my_app.config["UPLOAD_FOLDER"] = "uploads/"
    logger.start(
        logfile_name,
        level=level,
        format="{level} {time} {message}",
        backtrace=True,
        rotation="12:00",
        compression="zip",
    )
    logger.info(logfile_name)
    logger.warning(logfile_name)
    logger.error(logfile_name)
    my_app.logger.addHandler(journal.InterceptHandler())
    return my_app


logging.basicConfig(
    level=level,
    filename=logfile_name,
    format="%(levelname)s %(asctime)s %(module)s %(name)s %(message)s",
)


app = create_app()

app.register_blueprint(app_route)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
