# -*- coding: utf-8 -*-
from copy import deepcopy

from flask import Flask, Response
from flask.json import dumps
from werkzeug.exceptions import Aborter

abort = Aborter()


class JsonFlask(Flask):
    def dispatch_request(self, *args, **kwargs):
        status_code = 200
        result = {}

        try:
            result = super(JsonFlask, self).dispatch_request()
        except HTTPException as e:
            response = jsonify(status=e.status, status_code=e.http_code, msg=e.msg)
            return response
        except Exception as e:
            # 如果是werkzeug中抛出的HTTPException异常 werkzeug中的HTTPException都含有code成员变量
            if hasattr(e, 'code'):
                status_code = e.code
            else:
                # 日志交给errorhandler记录
                raise e
        if status_code != 200:
            abort(status_code)

        response = jsonify(result, status_code=status_code)

        return response


app = Flask(__name__)

UNKNOWN_ERROR = "2000"
TEST_STATUS = "1000"
ERR_MSG_MAP = {
    TEST_STATUS: "测试错误信息",
    UNKNOWN_ERROR: "未知错误"
}


@app.errorhandler(Exception)
def internal_error(e):
    resp = {
        'info': 'INTERNAL_ERROR',
        'status': '500'
    }
    return Response(dumps(resp), 500, mimetype='application/json')


@app.errorhandler(401)
def unauthorized_error(e):
    resp = {
        'info': 'UNAUTHORIZED',
        'status': '401'
    }
    return Response(dumps(resp), 401, mimetype='application/json')


class HTTPException(Exception):
    """
    HTTP异常
    """
    http_code = None
    status = UNKNOWN_ERROR
    msg = '请求异常'


class BadRequest(HTTPException):
    http_code = 400

    def __init__(self, status=None, msg=None):
        self.status = status
        self.msg = msg


@app.errorhandler(BadRequest)
def bad_request(e):
    response = jsonify(status=e.status, status_code=e.http_code, msg=e.msg)
    return response


common_resp = {
    "info": "Success",
    "status": "1"
}


def jsonify(raw=None, status=None, msg=None, status_code=200):
    copy_resp = deepcopy(common_resp)

    if raw is not None:
        copy_resp.update({'data': raw})
    if status is not None:
        resp_dict = {
            "info": ERR_MSG_MAP.get(status),
            "status": status
        }
        if msg:
            resp_dict["error_message"] = msg
        copy_resp.update(resp_dict)
    resp = Response(dumps(copy_resp), mimetype='application/json')
    resp.status_code = status_code
    resp.resp = copy_resp
    return resp


@app.route("/hello")
def hello():
    raise BadRequest(status=TEST_STATUS)
    data = {
        "hardware": 1,
        "b": 2
    }
    return data


@app.route("/world")
def world():
    b = 2
    a = b / 0
    return a


@app.route("/login")
def login():
    abort(401)
    return "hardware"


if __name__ == '__main__':
    app.run(debug=True)
