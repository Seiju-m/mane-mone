import os
from flask import Flask, request, Response, abort, render_template, redirect, jsonify, url_for
from flask_login import LoginManager, login_user, logout_user, login_required
from collections import defaultdict
# from user import users
from flask_sqlalchemy import SQLAlchemy
from lib import calc, user, db_ope
from test_db import init_db_func,reg_account_func

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = "secret"

# db_flg = os.path.exists('./db/manage2.db')
# if(db_flg == True):
#     pass
# else:
#     init_db_func()
#     reg_account_func()


# ユーザーチェックに使用する辞書作成
nested_dict = lambda: defaultdict(nested_dict)
user_check = nested_dict()
for i in user.users.values():
    user_check[i.name]["password"] = i.password
    user_check[i.name]["id"] = i.id

@login_manager.user_loader
def load_user(user_id):
    return user.users.get(int(user_id))

# ログインしないと表示されないパス
@app.route('/mana-mone/')
@login_required
def protected():
    return render_template("mana-mone.html")

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

@app.route('/update', methods=["POST"])
def upd():
    req = request.json
    if request.json.get('cat') == 'food':
        db_res = db_ope.upd_food(request.json.get('st_val'), request.json.get('ex_val'))
    elif request.json.get('cat') == 'daily':
        db_ope.upd_daily(request.json.get('st_val'), request.json.get('ex_val'))
    elif request.json.get('cat') == 'hobby':
        db_ope.upd_hobby(request.json.get('st_val'), request.json.get('ex_val'))
    elif request.json.get('cat') == 'rent':
        db_ope.upd_rent(request.json.get('st_val'))
    elif request.json.get('cat') == 'scholar':
        db_ope.upd_scholar(request.json.get('st_val'))
    elif request.json.get('cat') == 'util':
        db_ope.upd_util(request.json.get('st_val'))
    elif request.json.get('cat') == 'other':
        db_ope.upd_other(request.json.get('st_val'))
    elif request.json.get('cat') == 'income':
        db_ope.upd_income(request.json.get('st_val'))
    else:
        print('catagory is not set')
    res = jsonify({
        'status_code':200
    })
    return res


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))