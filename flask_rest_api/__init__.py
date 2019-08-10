# https://www.youtube.com/watch?v=PTZiDnuC86g
# intro to marshmallow by pp-> https://www.youtube.com/watch?v=S7Fh5XnuhPU + https://www.youtube.com/watch?v=kRNXKzfYrPU
from flask import Flask
from flask_rest_api.extensions import db, ma, migrate
from flask_rest_api.routes import main


def create_app(config_file="settings.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    app.register_blueprint(main)

    return app
