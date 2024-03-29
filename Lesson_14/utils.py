import email
from operator import and_

from sqlalchemy.orm import sessionmaker
from Lesson_14.models import Base
from Lesson_14.models import User, Product, Purchase, Profile, Address






def create_tables(engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def create_user(session, email, password):
    user = User(email=email, password=password)
    session.add(user)
    session.commit()
    return user

def add_address(session, new_address: str, new_city: str, user_id: int):
    address = Address(city=new_city, address=new_address, user_id=user_id)
    session.add(address)
    session.commit()


def update_address(session, old_address: str, old_city: str, new_address: str, new_city: str, user_id: int):
    session.query(Address).filter(and_(Address.address == old_address, Address.city == old_city,
                                       Address.user_id == user_id)).update({'city': f'{new_city}',
                                                                            'address': f'{new_address}'})
    session.commit()

def create_product(session, name, price, count, comment):
    product = Product(name=name, price=price, count=count, comment=comment)
    session.add(product)
    session.commit()
    return product


def find_user(session, email):
    return session.query(User).filter(User.email == email).first()

def add_purchase(session, user_id, product_id,count):
    purchase = Purchase(user_id=user_id, product_id = product_id, count=count)
    session.add(purchase)
    session.commit()
    return purchase


def delete_product(session, product_id):
    session.query(Product).filter_by(id=product_id).delete()
    session.commit()

def update_product(session,product_id, name, price,count, comment):
     session.query(Product).filter_by(id=product_id).update({"name": f"{name}", "price": f"{price}","count": f"{count}", "comment": f"{comment}"})
     session.commit()


def search_purchases_by_user(session, email):
    user_id = session.query(User.id).filter(User.email == email)
    result = session.query(Purchase).filter(Purchase.user_id == user_id)
    for it in result:
        return it



def search_product_by_user(session,user_id):

    session.query(Purchase).filter(Purchase.user_id == user_id)
    user_id = session.query(User.id).filter(User.email == email)
    result = session.query(Purchase).filter(Purchase.user_id == user_id).first()
    return result

def get_users(session):
    users = session.query(User).all()
    return [u.as_dict() for u in users]