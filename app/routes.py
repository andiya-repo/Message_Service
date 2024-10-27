from flask import jsonify
from app import app


@app.route('/')
def index():
    # for rule in app.url_map.iter_rules():
    #     if rule.endpoint not in Constants.permissions['admin']:
    #         print(rule.endpoint)
    return jsonify({'msg': 'Message Service Backend API'}), 200
