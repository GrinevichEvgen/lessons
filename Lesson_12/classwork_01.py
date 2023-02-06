from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists

from Lesson_12.models import Base, User

DB_USER = "evgen"
DB_PASSWORD = "evgen"
DB_NAME = "evgen"
DB_ECHO = True


if __name__ == "__main__":
    engine = create_engine(
          f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo = True,
)
    if not database_exists(engine.url):
        create_database(engine.url)


    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # user = User(email="test@test.com", password="password")
    # session.add(user)
    # session.commit()
