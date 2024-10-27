from app import db
from app.utils import Utils


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.String(16), primary_key=True, default=Utils.generate_new_id)
    created_at = db.Column(db.DateTime(), default=db.func.current_timestamp().op('AT TIME ZONE')('UTC'))
    updated_at = db.Column(db.DateTime(), default=db.func.current_timestamp().op('AT TIME ZONE')('UTC'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MessageService(BaseModel):
    __tablename__ = 'message_service'

    title = db.Column(db.String(255), nullable=False)
    summary = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    time = db.Column(db.DateTime(), nullable=False)
    seen = db.Column(db.Integer, default=1)
    entity_type = db.Column(db.String(255), nullable=False)
    entity_id = db.Column(db.String(255), nullable=False)
    message_type = db.Column(db.String(255), nullable=False)
