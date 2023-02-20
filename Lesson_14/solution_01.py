'''Подключить модели из предыдущего урока,
создать для каждой модели функцию (роут) при помощи flask приложения,
которая принимает POST запрос и создает соответствующий объект и запись в БД.'''


import logging
from flask import Flask, request
from sqlalchemy import create_engine
from Lesson_14.utils import create_tables, get_users, create_user, find_user, add_address, update_address, \
    create_product, update_product, delete_product
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

@app.route("/", methods=["GET"])
def user_find():
   return find_user(app.session)

app.route('/', methods=['POST'])


def profile_create():
    profile = create_profile(app.session, request.form.get('email'), request.form.get('city'),
                                      request.form.get('address'), request.form.get('phone'), request.form.get('age'))
    return {'profile_id': profile.id}


@app.route('/', methods=['POST'])
def address_add():
    location = add_address(app.session, request.form.get('email'), request.form.get('city'),
                                      request.form.get('address'))
    return {'location_id': location.id}

@app.route('/', methods=['POST'])
def address_update():
    location = update_address(app.session, request.form.get('email'), request.form.get('old_city'),
             request.form.get('old_address'), request.form.get('new_city'), request.form.get('new_address'))
    return {'location_id': location.id}

@app.route("/", methods=["POST"])
def product_create():
    product = create_product(app.session, request.form.get('name'), request.form.get('price'),
                                      request.form.get('count'), request.form.get('comment'))
    return {'product_id': product.id}

@app.route('/', methods=['POST'])
def product_update():
    product = update_product(app.session, request.form.get('product_id'), request.form.get('name'),
             request.form.get('price'), request.form.get('count'), request.form.get('comment'))
    return {'product_id': product.id}

@app.route('/', methods=['POST'])
def product_delete():
    product = delete_product(app.session, request.form.get('product_id'))



if __name__ == "__main__":
    engine = create_engine("postgresql://evgen:evgen@localhost/evgen")
    app.session = create_tables(engine)
    app.run()