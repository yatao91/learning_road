# coding: utf-8

from flask_script import Server, Manager
from flask_script.commands import ShowUrls

from app import create_app

app = create_app()


app.debug = True
manager = Manager(app)

manager.add_command("runserver", Server('0.0.0.0', port=8000, threaded=True))

manager.add_command("show_urls", ShowUrls())


if __name__ == "__main__":
    manager.run()
