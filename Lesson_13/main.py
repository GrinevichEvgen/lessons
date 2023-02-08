import logging
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from Lesson_13.models import Purchase
from Lesson_13.utils import create_user, create_product, find_user, add_purchase, search_purchases_by_user, delete_product, update_product, create_tables

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


DB_USER = "evgen"
DB_PASSWORD = "evgen"
DB_NAME = "evgen"
DB_ECHO = True



if __name__ == "__main__":
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}",
    )
    if not database_exists(engine.url):
        create_database(engine.url)

    session = create_tables(engine)


    def select_purchase(user_id):
        selection = session.query(Purchase).filter_by(user_id=user_id).all()
        for user_data in selection:
            print(user_data.id, user_data.user_id, user_data.product_id)
    menu ='''
        1 .Создать пользователя
        2. Найти пользователя
        3. Добавить товар
        4. Добавить покупку
        5. Ввывод всех товаров, купленных определенным пользователем (only one!!)
        6 .Удалить продукт
        7. Обновить продукт
        8. EXIT
    '''
    while True:

        logger.info(menu)
        print()
        choice = input("выберите действие:  ")

        if choice == "1":
            email = input('Введите почту')
            password = input('Введите пароль ')
            user = create_user(session, email, password)
            logger.info(f'пользователь  #{user.id} создан')


        if choice == "2":
            email = input('Введите электронную почту ')
            user = find_user(session, email)
            logger.info(f'пользователь  # {user.id} найден')

        if choice == "3":
            name = input('Введите название продукта ')
            price = float(input('Введите цену '))
            count = int(input('Введите количество '))
            comment = input('Введите комментарий ')
            product = create_product(session, name, price, count, comment)
            logger.info(f'продукт  #{product.id} создан')

        if choice == "4":
            user_id = int(input('Введите id пользователя: '))
            product_id = int(input('Введите id продукта: '))
            count = int(input('Введите количество продукта: '))
            purchase = add_purchase(session, user_id, product_id, count)
            logger.info(f'покупка   {purchase.id} создана ')

        if choice == "5":
            email = input('Введите email пользователя ')
            purchase = search_purchases_by_user(session, email)
            logger.info(f'{purchase.user.email}, {purchase.product.name}, количество {purchase.count}')

        if choice == "6":
            product_id = input('Введите ID продукта ')
            product = delete_product(session, product_id)
            logger.info(f'Продукт #{product_id} удален ')

        if choice == "7":
            product_id = int(input('Введите id продукта: '))
            name = input('Введите название продукта: ')
            price = float(input('Введите цену продукта: '))
            count = int(input('Введите количество продукта'))
            comment = input('Введите комментарий')
            update_product(session, product_id, name, price, count, comment)
            logger.info(f'Продукт #{product_id} update ')

        elif choice == "8":
            exit()