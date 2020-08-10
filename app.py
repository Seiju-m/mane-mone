import os
from flask import Flask, request, Response, abort, render_template, redirect, jsonify, url_for
from flask_login import LoginManager, login_user, logout_user, login_required
from collections import defaultdict
import json
# from user import users
import datetime
from dateutil.relativedelta import relativedelta
from flask_sqlalchemy import SQLAlchemy
from lib import calc, user, db_ope
# from test_db import init_db_func,reg_account_func

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = "secret"

# ユーザーチェックに使用する辞書作成
nested_dict = lambda: defaultdict(nested_dict)
user_check = nested_dict()
for i in user.users.values():
    user_check[i.name]["password"] = i.password
    user_check[i.name]["id"] = i.id

# nextをクリックで、axiosでここまで飛ばし、もともと日付から取得した
# 変数に1増減させて変数を更新する。
# その値でdbから引っ張る、なければありませんを表示（からのぱい？）


@login_manager.user_loader
def load_user(user_id):
    return user.users.get(int(user_id))

# ログインしないと表示されないパス
# @app.route('/mana-mone/')
# @login_required
# def protected():
#     return render_template("mana-mone.html")

# ログインパス
@app.route('/', methods=["GET", "POST"])
def login():
    if(request.method == "POST"):
        # ユーザーチェック
        if(request.form["username"] in user_check and request.form["password"] == user_check[request.form["username"]]["password"]):
            # ユーザーが存在した場合はログイン
            login_user(user.users.get(user_check[request.form["username"]]["id"]))
            return redirect(url_for('main'))
        else:
            return abort(401)
    else:
        return render_template("login.html")

@app.route('/main/')
@login_required
def main():
    data = db_ope.get_account()
    n_data = calc.calc(data)
    return render_template("mana-mone.html",  data=n_data)

# ログアウトパス
@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return render_template("logout.html")

# initialize monthly
dt_now = datetime.datetime.now()
default_month = str(dt_now.year) + str((dt_now - relativedelta(months=1)).strftime('%m'))
# new_month = default_month

# 月次レポート
@app.route('/monthly/', methods=["GET"])
@login_required
def monthly():
    month = db_ope.query_month(default_month)
    if month is None:
        class Month:
            def __init__(self):
                self.food_ex = 0
                self.income = 0
                self.daily_ex = 0
                self.hobby_ex = 0
                self.transport_ex= 0
                self.other_ex= 0
                self.last_ex= 0
                self.rent_cost= 0
                self.scholar= 0
                self.utility_cost= 0
                self.commu= 0
                self.month= 0

        month = Month()

    data = db_ope.get_account()
    n_data = calc.calc(data)

    return render_template("monthly.html", month=month, data=n_data)

@app.route('/prev-month/', methods=["POST"])
@login_required
def prev_month():
    month = db_ope.query_month(int(request.json.get('month'))-1)
    if month is None:
        res = jsonify({
            'status_code':201,
            'income': 0,
            'food': 0,
            'daily': 0,
            'hobby': 0,
            'transport': 0,
            'other': 0,
            'last': 0,
            'rent': 0,
            'scholar': 0,
            'utility': 0,
            'commu': 0,
            'month': 'データがありません',
        })
    else:
        res = jsonify({
            'status_code':200,
            'income': month.income,
            'food': month.food_ex,
            'daily': month.daily_ex,
            'hobby': month.hobby_ex,
            'transport': month.transport_ex,
            'other': month.other_ex,
            'last': month.last_ex,
            'rent': month.rent_cost,
            'scholar': month.scholar,
            'utility': month.utility_cost,
            'commu': month.commu,
            'month': month.month,
        })
    return res


@app.route('/next-month/', methods=["POST"])
@login_required
def next_month():
    month = db_ope.query_month(int(request.json.get('month'))+1)
    if month is None:
        res = jsonify({
            'status_code':201,
            'income': 0,
            'food': 0,
            'daily': 0,
            'hobby': 0,
            'transport': 0,
            'other': 0,
            'last': 0,
            'rent': 0,
            'scholar': 0,
            'utility': 0,
            'commu': 0,
            'month': 'データがありません',
        })
    else:
        res = jsonify({
            'status_code':200,
            'income': month.income,
            'food': month.food_ex,
            'daily': month.daily_ex,
            'hobby': month.hobby_ex,
            'transport': month.transport_ex,
            'other': month.other_ex,
            'last': month.last_ex,
            'rent': month.rent_cost,
            'scholar': month.scholar,
            'utility': month.utility_cost,
            'commu': month.commu,
            'month': month.month,
        })
    return res

# 月次レポート
@app.route('/createReport/', methods=["POST"])
@login_required
def createReport():
    #try:
    print("-----------------------------")
    month = request.json.get('month')
    last = request.json.get('last')
    print(last)
    # month = db_ope.query_month(int(request.json.get('month')))
    month_check = db_ope.query_month(month)
    if month_check is None:
        data = db_ope.get_account()
        db_ope.add_month(data.income,data.food_ex,data.daily_ex,data.hobby_ex,
            data.transport_ex,data.other_ex,last,data.rent_cost,data.scholar,
            data.utility_cost,data.commu,int(month))
        res = jsonify({
            'status_code':200,
            'income': data.income,
            'food': data.food_ex,
            'daily': data.daily_ex,
            'hobby': data.hobby_ex,
            'transport': data.transport_ex,
            'other': data.other_ex,
            'last': last,
            'rent': data.rent_cost,
            'scholar': data.scholar,
            'utility': data.utility_cost,
            'commu': data.commu,
            'month': month
        })
    else:
        res = jsonify({
            'status_code':500
        })

    return res


@app.route('/update', methods=["POST"])
def upd():
    req = request.json
    if request.json.get('cat') == 'food':
        db_ope.upd_ex(request.json.get('st_val'), request.json.get('ex_val'),'food')
    elif request.json.get('cat') == 'daily':
        db_ope.upd_ex(request.json.get('st_val'), request.json.get('ex_val'),'daily')
    elif request.json.get('cat') == 'hobby':
        db_ope.upd_ex(request.json.get('st_val'), request.json.get('ex_val'),'hobby')
    elif request.json.get('cat') == 'rent':
        db_ope.upd_ex(request.json.get('st_val'), '' ,'rent')
    elif request.json.get('cat') == 'scholar':
        db_ope.upd_ex(request.json.get('st_val'), '' ,'scholar')
    elif request.json.get('cat') == 'util':
        db_ope.upd_ex(request.json.get('st_val'), '' ,'util')
    elif request.json.get('cat') == 'other':
        db_ope.upd_ex(request.json.get('st_val'), request.json.get('ex_val'),'other')
    elif request.json.get('cat') == 'income':
        db_ope.upd_ex(request.json.get('st_val'), '' ,'income')
    elif request.json.get('cat') == 'transport':
        db_ope.upd_ex(request.json.get('st_val'), request.json.get('ex_val'),'transport')
    elif request.json.get('cat') == 'commu':
        db_ope.upd_ex(request.json.get('st_val'), '' ,'commu')
    else:
        print('catagory is not set')
    res = jsonify({
        'status_code':200
    })
    return res

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))