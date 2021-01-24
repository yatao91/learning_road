# -*- coding: utf-8 -*-
import uuid

from flask import Flask, make_response, session, request

app = Flask(__name__)
app.secret_key = "aaaabbbccc"


@app.route("/cookie")
def cookie():
    response = make_response("hello world")
    username = session.get("username")
    key = "_ANONYMOUSUSER"
    anonymous_user = request.cookies.get(key)
    # 1.用户登录
    if username:
        print("用户处于登录状态")
        return response
    # 2.用户未登录
    else:
        # 2.1.同一匿名用户,不重新生成cookie,直接续租
        if anonymous_user:
            print("匿名用户处于二次访问状态")
            response.set_cookie(key=key, value=anonymous_user, max_age=60 * 60)
            return response
        # 2.2.新匿名用户,新生成cookie,并设置有效期
        else:
            print("匿名用户首次访问状态")
            value = "user_" + uuid.uuid4().hex
            response.set_cookie(key=key, value=value, max_age=60 * 60)
            return response


@app.route("/login")
def login():
    print("用户登录")
    session["username"] = "suyatao"
    return "login"


@app.route("/logout")
def logout():
    print("用户退出登录")
    session.pop("username")
    return "logout"


if __name__ == '__main__':
    app.run(debug=True)
