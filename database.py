from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_cat(name):
    cat_object = Cat(name=name)
    cat_object.vote = 0
    session.add(cat_object)
    session.commit()

def get_cat_by_id(id):
	cat_object= session.query(Cat).filter_by(id=id).first()
	return cat_object.name

def add_vote(id):
	cat_object = session.query(Cat).filter_by(id=id).first()
	cat_object.vote += 1
	session.commit()

def get_all_cats():
    cats = session.query(Cat).all()
    return cats