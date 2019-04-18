from flask import Flask, request,jsonify
from setting import MONGO_DB

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    # username = request.form.get("username")
    # password = request.form.get("password")
    user_info = request.form.to_dict()
    print(user_info)
    user = MONGO_DB.users.find_one(user_info)
    if user:
        return jsonify({"status": 200, "msg": f"欢迎{user.get('username')}登陆"})
    else:
        return jsonify({"status": 201, "msg": "用户密码错误"})


if __name__ == '__main__':
    app.run("0.0.0.0",9527,debug=True)