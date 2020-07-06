import os
from flask import Flask, request, Response, abort, render_template, redirect
from flask_login import LoginManager, login_user, logout_user, login_required
from collections import defaultdict
from user import users
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = "secret"

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/manage.db'

class User(db.Model):
    user = db.Column(db.String, primary_key=True)
    income = db.Column(db.Integer, nullable=False)
    food_ex = db.Column(db.Integer, nullable=False)
    daily_ex = db.Column(db.Integer,  nullable=False)
    hobby_ex = db.Column(db.Integer,  nullable=False)
    last_ex = db.Column(db.Integer,  nullable=False)
    rent_cost = db.Column(db.Integer, nullable=False)
    scholar = db.Column(db.Integer, nullable=False)
    utility_cost = db.Column(db.Integer, nullable=False)
    other = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.user

# ユーザーチェックに使用する辞書作成
nested_dict = lambda: defaultdict(nested_dict)
user_check = nested_dict()
for i in users.values():
    user_check[i.name]["password"] = i.password
    user_check[i.name]["id"] = i.id

@login_manager.user_loader
def load_user(user_id):
    return users.get(int(user_id))

# ログインしないと表示されないパス
@app.route('/mana-mone/')
@login_required
def protected():
    #data = User.query.filter_by(user='tfjkv').first()
    data = 500
    return render_template("mana-mone.html", data=data)

# ログインパス
@app.route('/', methods=["GET", "POST"])
def login():
    if(request.method == "POST"):
        # ユーザーチェック
        if(request.form["username"] in user_check and request.form["password"] == user_check[request.form["username"]]["password"]):
            # ユーザーが存在した場合はログイン
            login_user(users.get(user_check[request.form["username"]]["id"]))
            return render_template("mana-mone.html")
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



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))