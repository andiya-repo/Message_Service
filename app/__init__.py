from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS



app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
CORS(app)


from app.message import message_bp

app.register_blueprint(message_bp, url_prefix="/message_service")



from app import routes