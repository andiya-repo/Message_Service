from flask import Blueprint

message_bp = Blueprint('message', __name__)

from app.message import routes
