from flask import Blueprint

bp = Blueprint("main", __name__)

from . import routes  # noqa: F401, E402


