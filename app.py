import os
from flask import Flask, request, Response, abort, render_template, redirect, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required
from collections import defaultdict
# from user import users
from flask_sqlalchemy import SQLAlchemy
from lib import calc, user, db_ope
# import lib
# from lib import db_ope

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
            data = db_ope.get_account()
            # data = User.query.filter_by(user='tfjkv').first()
            n_data = calc.calc(data)
            return render_template("mana-mone.html",  data=n_data)
        else:
            return abort(401)
    else:
        return render_template("login.html")

# ログアウトパス
@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return render_template("logout.html")

@app.route('/food', methods=["POST"])
def food():
    req = request.json
    print("req" + str(req))
    print(request.json.get('food_st_e'))
    db_ope.upd_food(request.json.get('food_st_e'), request.json.get('food_ex_e'))
    res = jsonify({
        'status_code':200
    })
    return res


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))