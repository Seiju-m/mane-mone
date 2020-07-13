from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import re

DATABASE = 'postgresql'
USER = 'efqweasvzdxqaw'
PASSWORD = '00cd7ce89b1fb2069a069f42dc11781a857273a9ac080e08ff9b3441c663af94'
HOST = 'ec2-34-230-149-169.compute-1.amazonaws.com'
PORT = '5432'
DB_NAME = 'deiun42i8fk52p'

CONNECT_STR = '{}://{}:{}@{}:{}/{}'.format(DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

# database_file = os.path.join(os.path.abspath(os.path.dirname(__file__) + '/../db'), 'manage2.db')
engine = create_engine(CONNECT_STR, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import db.models
    Base.metadata.create_all(bind=engine,checkfirst=True)

def get_account():
    import db.models as db
    data = db_session.query(db.Account).filter(db.Account.id == 'tfjkv').first()
    return data

def reg_account():
    import db.models as db
    content = db.Account('tfjkv', 181608, 0, 20000, 0, 5000, 0, 20000, 0, 54860, 16700, 0, 0)
    db_session.add(content)
    db_session.commit()

def query_all():
    import db.models as db
    user = db.Account.query.all()
    print('all:' + str(user))

def upd_income(income):
    import db.models as db
    data = db_session.query(db.Account).filter(db.Account.id == 'tfjkv').first()
    data.income = income
    db_session.commit()

def upd_food(food_st, food_ex):
    import db.models as db
    data = db_session.query(db.Account).filter(db.Account.id == 'tfjkv').first()
    data.food_st = food_st
    data.food_ex = food_ex
    db_session.commit()
    return 'res'

def upd_daily(daily_st, daily_ex):
    import db.models as db
    data = db_session.query(db.Account).filter(db.Account.id == 'tfjkv').first()
    data.daily_st = daily_st
    data.daily_ex = daily_ex
    db_session.commit()

def upd_hobby(hobby_st, hobby_ex):
    import db.models as db
    data = db_session.query(db.Account).filter(db.Account.id == 'tfjkv').first()
    data.hobby_st = hobby_st
    data.hobby_ex = hobby_ex
    db_session.commit()

def upd_rent(rent_cost):
    import db.models as db
    data = db_session.query(db.Account).filter(db.Account.id == 'tfjkv').first()
    data.rent_cost = rent_cost
    db_session.commit()

def upd_scholar(scholar):
    import db.models as db
    data = db_session.query(db.Account).filter(db.Account.id == 'tfjkv').first()
    data.scholar = scholar
    db_session.commit()

def upd_util(utility_cost):
    import db.models as db
    data = db_session.query(db.Account).filter(db.Account.id == 'tfjkv').first()
    data.utility_cost = utility_cost
    db_session.commit()

def upd_other(other):
    import db.models as db
    data = db_session.query(db.Account).filter(db.Account.id == 'tfjkv').first()
    data.other = other
    db_session.commit()
