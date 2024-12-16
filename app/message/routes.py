from flask import request, jsonify
import requests
from app.message import message_bp
from app.models import *
from sqlalchemy import and_
from datetime import datetime
import jdatetime


@message_bp.route('/add', methods=['POST'])
def message_add():
    title = request.json.get('title', None)
    summary = request.json.get('summary', None)
    description = request.json.get('description', None)
    time = request.json.get('time', None)
    entity_type = request.json.get('entity_type', None)
    entity_id = request.json.get('entity_id', None)
    message_type = request.json.get('message_type', None)
    push = request.json.get('push', None)
    event = request.json.get('event', None)

    message = MessageService(title=title, summary=summary, description=description, time=time,
                             entity_type=entity_type, entity_id=entity_id, message_type=message_type)
    db.session.add(message)
    db.session.commit()

    if push == 1:
        base_url = f"http://185.105.187.116:7008/api/v1/push/broadcast/{event}"
        current_time = datetime.now()
        time_string = current_time.strftime('%Y-%m-%d %H:%M:%S')
        gregorian_datetime = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')
        jalali_datetime = jdatetime.datetime.fromgregorian(datetime=gregorian_datetime)
        jalali_time_string = jalali_datetime.strftime('%Y-%m-%d %H:%M:%S')
        # print(jalali_time_string)


        data = {
            "title": title,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "message_type": message_type,
            "time": jalali_time_string,
            "summary": summary

        }

        response = requests.post(base_url, json=data)

    return jsonify({'message': 'Successfully added message', "data": None, "success": True}), 200


@message_bp.route('/list', methods=['GET'])
def message_list():

    page = int(request.args.get('page', 1))
    page -= 1
    limit = int(request.args.get('limit', 3))

    message_filter = []

    message_filter.append(
        MessageService.entity_type.like(f'%{request.args["entity_type"]}%')) if request.args.get("entity_type",
                                                                                                 False) else None

    message_filter.append(
        MessageService.entity_id.like(f'%{request.args["entity_id"]}%')) if request.args.get("entity_id",
                                                                                             False) else None

    message_filter.append(
        MessageService.message_type.like(f'%{request.args["message_type"]}%')) if request.args.get("message_type",
                                                                                                   False) else None

    message = db.session.query(MessageService).filter(and_(*message_filter)).order_by(
        MessageService.time.desc()).offset(page * limit).limit(limit).all()

    if message is None:
        return jsonify({'msg': 'Not found message', "data": None, "success": False}), 404

    msg_list = []
    for msg in message:
        msg = msg.__dict__
        del msg['_sa_instance_state']
        del msg['description']

        time_string = msg['time'].strftime('%Y-%m-%d %H:%M:%S')
        gregorian_datetime = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')
        jalali_datetime = jdatetime.datetime.fromgregorian(datetime=gregorian_datetime)
        jalali_time_string = jalali_datetime.strftime('%Y-%m-%d %H:%M:%S')
        msg['time'] = jalali_time_string
        msg_list.append(msg)

    return jsonify({"message": "Successfully shows list", "data": msg_list, "success": True}), 200


@message_bp.route('/get/<message_id>', methods=['GET'])
def carrier_get(message_id):
    message = db.session.query(MessageService).filter(MessageService.id == message_id).first()

    if message is None:
        return jsonify({'msg': 'Not found message', "data": None, "success": False}), 404

    message = message.__dict__
    del message['_sa_instance_state']

    return jsonify({"message": "Successfully shows detail", "data": message, "success": True}), 200


@message_bp.route('/delete/<message_id>', methods=['DELETE'])
def message_delete(message_id):
    message_to_delete = db.session.query(MessageService).filter(MessageService.id == message_id).first()

    if message_to_delete is None:
        return jsonify({'msg': 'Message not found.', "data": None, "success": False}), 404

    db.session.delete(message_to_delete)
    db.session.commit()

    return jsonify({'msg': 'Message was deleted', "data": None, "success": False}), 200
