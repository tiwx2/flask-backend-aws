from flask import Blueprint

bp = Blueprint('main', __name__)

from flaskbackend.main import routes