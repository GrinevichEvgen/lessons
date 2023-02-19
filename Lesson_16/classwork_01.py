import logging
from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
import utils1

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
loger = logging.getLogger(__name__)

DB_USER = "evgen"
DB_PASSWORD = "evgen"
DB_NAME = "evgen"
DB_ECHO = True


if __name__ == "__main__":
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}")
    if not database_exists(engine.url):
        create_database(engine.url)

    session = utils1.create_tables(engine)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        for ids in request.args.to_dict().values():
            response = utils1.find_user(session=session, ids=int(ids))
            loger.info(f'{response}')
    elif request.method == "POST":
        utils1.create_user(session=session,
                          email=request.form.to_dict()['email'],
                          password=request.form.to_dict()['password'],
                          phone=request.form.to_dict()['phone'],
                          age=int(request.form.to_dict()['age']))
    return 'homework'


if __name__ == "__main__":
    app.run()