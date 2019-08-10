import os

basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = os.environ.get("SECRET_KEY") or "secret key or something"
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or f"sqlite:///{os.path.join(basedir, 'database.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
