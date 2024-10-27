import json
import app


class Config:
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = 'message_service_project_0241#$'
    SQLALCHEMY_DATABASE_URI = 'postgresql://myuser:mypassword@185.105.187.115/message_service'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {'json_serializer': lambda obj: json.dumps(obj, ensure_ascii=False)}
    JSON_AS_ASCII = False
    TRAP_HTTP_EXCEPTIONS = True
    # LANGUAGES = ['en', 'fa', 'ar']
    PROJECT_ROOT = '/srv/message_service/'
    SEND_FILE_MAX_AGE_DEFAULT = 0
    # ELASTICSEARCH_CLIENT = app.es
