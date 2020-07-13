from lib.db_ope import init_db, get_account, query_all, reg_account,upd_food
import os

# os.remove('db/manage2.db')

print('before init')

def init_db_func():
    init_db()

def reg_account_func():
    reg_account()

# account = get_account()
# print(account)

# query_all()

# upd_food(10000, 5000)