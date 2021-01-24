# -*- coding: utf-8 -*-
from werkzeug.wrappers import Response, Request


@Request.application
def application(request):
    return Response('Hello world')


if __name__ == '__main__':
   from werkzeug.serving import run_simple
   run_simple('0.0.0.0', 4000, application)