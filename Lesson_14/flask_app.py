import logging
from flask import Flask, request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        logger.info("Обрабатываю POST запрос")
        return request.form.to_dict()

    for key, item in request.args.to_dict().items():  # надо вернуть ключ занчение парами
        logger.info(f"{key}={item}")
    logger.info("Обрабатываю GET запрос")
    return request.args.to_dict()


if __name__ == "__main__":
    app.run()
