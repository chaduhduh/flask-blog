import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


engine = create_engine('sqlite:////var/www/flask_blog/flask_blog/flask_blog.db')
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from database_setup import(
        Base,
        Items as Item,
        Users as User,
        Categories as Categories
        )
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

def seed_categories(engine):
    # populate our categories
    # Seed Categories
    engine.execute("""
	 DELETE FROM Categories where 1 = 1;
    """)
    engine.execute("""
        INSERT INTO Categories (name) values
            ("Music"),
            ("Sports"),
            ("Entertainment"),
            ("Dining"),
            ("Funny")
    """)
