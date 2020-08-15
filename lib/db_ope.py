from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import re
import datetime
import pytz

## for prod
DATABASE = 'postgresql'
USER = 'rsownwafjdissl'
PASSWORD = '04bbfe55fd79187e75d3256230844b9f0e4a2e396a40db8977e4e1e05760c177'
HOST = 'ec2-34-230-149-169.compute-1.amazonaws.com'
PORT = '5432'
DB_NAME = 'dar8qtfcfi65mk'

## for dev
# DATABASE = 'postgresql'
# USER = 'postgres'
# PASSWORD = 'Seiju7479'
# HOST = '127.0.0.1'
# PORT = '5432'
# DB_NAME = 'manage3'

## connect info
CONNECT_STR = '{}://{}:{}@{}:{}/{}'.format(DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

## db info
engine = create_engine(CONNECT_STR, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import db.models
    Base.metadata.create_all(bind=engine,checkfirst=True)

def get_account():
    import db.models as db
    data = db_session.query(db.Account).filter(db.Account.myuser == 'tfjkv').first()
    return data

def reg_account():
    import db.models as db
    content = db.Account('tfjkv', 181608, 0, 20000, 0, 5000, 0, 20000, 0, 54860, 16700, 0, 0)
    db_session.add(content)
    db_session.commit()

def reg_account2():
    import db.models as db
    content = db.Account('tfjkvar', 181608, 0, 20000, 0, 5000, 0, 20000, 0, 54860, 16700, 0, 0)
    db_session.add(content)
    db_session.commit()

def query_all():
    import db.models as db
    user = db.Account.query.all()
    print('all:' + str(user))

def query_month(month):
    import db.models as db
    data = db_session.query(db.Monthly).filter(db.Monthly.month == month).first()
    return data

def add_month(income, food_ex, daily_ex, hobby_ex, transport_ex, other_ex, 
last_ex, rent_cost, scholar, utility_cost, commu, month):
    import db.models as db
    #print("month" + str(month))
    content = db.Monthly(income, food_ex, daily_ex, hobby_ex, transport_ex,
     other_ex,  last_ex, rent_cost, scholar,utility_cost, commu, month)
    db_session.add(content)
    db_session.commit()

def upd_ex(st, ex, cat):
    import db.models as db
    data = db_session.query(db.Account).filter(db.Account.myuser == 'tfjkv').first()

    if cat in {'food'}:
        data.food_st = st
        data.food_ex = ex
    if cat in {'daily'}:
        data.daily_st = st
        data.daily_ex = ex
    if cat in {'hobby'}:
        data.hobby_st = st
        data.hobby_ex = ex
    if cat in {'transport'}:
        data.transport_st = st
        data.transport_ex = ex
    if cat in {'other'}:
        data.other_st = st
        data.other_ex = ex
    if cat in {'rent'}:
        data.rent_cost = st   
    if cat in {'income'}:
        data.income = st
    if cat in {'scholar'}:
        data.scholar = st
    if cat in {'util'}:
        data.utility_cost = st
    if cat in {'commu'}:
        data.commu = st

    dt_now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    data.update_date = dt_now.strftime('%Y/%m/%d %H:%M:%S')
    db_session.commit()
    return 'res'





