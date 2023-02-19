'''Подключить модели из предыдущего урока,
создать для каждой модели функцию (роут) при помощи flask приложения,
которая принимает POST запрос и создает соответствующий объект и запись в БД.'''


import logging
from flask import Flask, request
from sqlalchemy import create_engine
from Lesson_14.utils import create_tables, get_users, create_user
from Lesson_14.models import User, Product, Purchase, Profile, Address

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = Flask(__name__)

@app.route("/", methods=["GET"])
def users_get():
    return get_users(app.session)

@app.route("/", methods=["POST"])
def users_post():
    user = create_user(app.session, request.form.get("email"), request.form.get("password"))
    return {"user_id": user.id}



if __name__ == "__main__":
    engine = create_engine("postgresql://evgen:evgen@localhost/evgen")
    app.session = create_tables(engine)
    app.run()