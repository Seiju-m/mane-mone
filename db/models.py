from sqlalchemy import Column, String, Integer, Date
from lib.db_ope import Base
import datetime

dt_now = datetime.datetime.now()


class Account(Base):
    __tablename__ = 'account'
    # id = Column(String, primary_key=True)
    myuser = Column(String, primary_key=True)
    income = Column(Integer, nullable=False)
    food_ex = Column(Integer, nullable=False)
    food_st = Column(Integer, nullable=False)
    daily_ex = Column(Integer,  nullable=False)
    daily_st = Column(Integer,  nullable=False)
    hobby_ex = Column(Integer,  nullable=False)
    hobby_st = Column(Integer,  nullable=False)
    transport_ex = Column(Integer,  nullable=False)
    transport_st = Column(Integer,  nullable=False)
    other_ex = Column(Integer,  nullable=False)
    other_st = Column(Integer,  nullable=False)
    last_ex = Column(Integer,  nullable=False)
    rent_cost = Column(Integer, nullable=False)
    scholar = Column(Integer, nullable=False)
    utility_cost = Column(Integer, nullable=False)
    commu = Column(Integer, nullable=False)
    update_date = Column(Date)
    # id = Column(String)

    def __init__(self, myuser='tfjkv', income=181608, food_ex=0, food_st=20000,
     daily_ex=0, daily_st=5000,hobby_ex=0, hobby_st=20000,transport_ex=0,transport_st=25000,
     other_ex=0, other_st=5000,last_ex=0,rent_cost=54860,
     scholar=16700,utility_cost=0,commu=0, update_date=dt_now.strftime('%Y年%m月%d日 %H:%M:%S')):
        self.myuser = myuser
        self.income = income
        self.food_ex = food_ex
        self.food_st = food_st
        self.daily_ex = daily_ex
        self.daily_st = daily_st
        self.hobby_ex = hobby_ex
        self.hobby_st = hobby_st
        self.transport_ex = transport_ex
        self.transport_st = transport_st
        self.other_ex = other_ex
        self.other_st = other_st
        self.last_ex = last_ex
        self.rent_cost = rent_cost
        self.scholar = scholar
        self.scholar = scholar
        self.utility_cost = utility_cost
        self.commu = commu

    def __repr__(self):
        return '<User %r>' % self.myuser


class Monthly(Base):
    __tablename__ = 'monthly'
    income = Column(Integer, nullable=False)
    food_ex = Column(Integer, nullable=False)
    daily_ex = Column(Integer,  nullable=False)
    hobby_ex = Column(Integer,  nullable=False)
    transport_ex = Column(Integer,  nullable=False)
    other_ex = Column(Integer,  nullable=False)
    last_ex = Column(Integer,  nullable=False)
    rent_cost = Column(Integer, nullable=False)
    scholar = Column(Integer, nullable=False)
    utility_cost = Column(Integer, nullable=False)
    commu = Column(Integer, nullable=False)
    month = Column(Integer, primary_key=True)
    # month_id = Column(Integer, primary_key=True)
    # id = Column(String)

    def __init__(self, income=181608, food_ex=0,daily_ex=0,hobby_ex=0, transport_ex=0,
     other_ex=0, last_ex=0,rent_cost=54860, scholar=16700,utility_cost=0,commu=0,month=202007, month_id=000000):
        self.income = income
        self.food_ex = food_ex
        self.daily_ex = daily_ex
        self.hobby_ex = hobby_ex
        self.transport_ex = transport_ex
        self.other_ex = other_ex
        self.last_ex = last_ex
        self.rent_cost = rent_cost
        self.scholar = scholar
        self.scholar = scholar
        self.utility_cost = utility_cost
        self.commu = commu
        self.month = month
        # self.month_id = month_id

    def __repr__(self):
        return '<Month %r>' % self.month