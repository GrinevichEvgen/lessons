import logging

from flask import Flask, request
from sqlalchemy import create_engine

import utils1

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
loger = logging.getLogger(__name__)

DB_USER = "evgen"
DB_PASSWORD = "evgen"
DB_NAME = "evgen"
DB_ECHO = True


# @app.route("/", methods=["GET"])
# def index():
# return 'Start page!'

@app.route("/get_users/", methods=["GET"])
def get_users():
    response = utils1.find_user(session=app.session)
    return [user.email for user in response]


@app.route("/add_product/", methods=["POST"])
def add_product():
    utils1.add_product(session=app.session,
                       name=request.form.to_dict()['name'],
                       price=float(request.form.to_dict()['price']),
                       quantity=int(request.form.to_dict()['quantity']),
                       comment=request.form.to_dict()['comment'])
    return f'Product {request.form.to_dict()["name"]} added'


@app.route("/add_user/", methods=["POST"])
def add_user():
    utils1.create_user(session=app.session, email=request.form.to_dict()['email'],
                       password=request.form.to_dict()['password'], phone=request.form.to_dict()['phone'],
                       age=int(request.form.to_dict()['age']))
    return f'User {request.form.to_dict()["email"]} added'


@app.route("/get_products/", methods=["GET"])
def get_product():
    response = utils1.read_products(session=app.session)
    return [product.name for product in response]


@app.route("/update_product/", methods=["POST"])
def update_product():
    utils1.update_product(session=app.session, id_prod=int(request.form.to_dict()['id_prod']),
                          name=request.form.to_dict()['name'], price=float(request.form.to_dict()['price']),
                          quantity=int(request.form.to_dict()['quantity']), comment=request.form.to_dict()['comment'])
    return f'Product {request.form.to_dict()["name"]} updated.'


@app.route("/delete_product/", methods=["POST"])
def delete_product():
    utils1.delete_product(session=app.session, id_prod=int(request.form.to_dict()['id_prod']))
    return 'Product deleted.'


@app.route("/add_purchase/", methods=["POST"])
def add_purchase():
    utils1.add_purchase(session=app.session, user_id=int(request.form.to_dict()['user_id']),
                        prod_id=int(request.form.to_dict()['prod_id']),
                        quantity=int(request.form.to_dict()['quantity']))
    return f'Purchase added'


@app.route("/search_user_purchases/", methods=["GET"])
def get_user_purchases():
    response = utils1.search_purchase_by_user(session=app.session, user_id=int(request.args.to_dict()['user_id']))
    return [(product.product.name, product.quantity) for product in response]


@app.route("/filter_by_price/", methods=["GET"])
def filter_by_price():
    response = utils1.search_users_by_purchase_price(session=app.session, price=float(request.args.to_dict()['price']))
    return [(data.email, data.name) for data in response]


if __name__ == "__main__":
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}")
    app.session = utils1.create_tables(engine)
    app.run()
