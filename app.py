import os
from flask import Flask, request, Response, abort, render_template
from flask_login import LoginManager, login_user, logout_user, login_required
from collections import defaultdict
from user import users

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = "secret"

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
    return render_template("mana-mone.html")

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
    return Response('''
    logout success!<br />
    <a href="/">login</a>
    ''')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))