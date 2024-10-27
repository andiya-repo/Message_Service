import string
import secrets
from datetime import datetime
import datetime
from enum import Enum



class Utils:

    @staticmethod
    def unixtimestamp(return_string=False):
        return int(datetime.datetime.now().timestamp()) if not return_string else datetime.datetime.now().strftime(
            "%Y/%m/%d %H:%M:%S")

    @staticmethod
    def random_string(n=6):
        return ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(n))


    @staticmethod
    def generate_new_id():
        return Constance.app_prefix + "_" + Utils.random_string() + "_" + str(Utils.unixtimestamp())[-4:]


class EntityType(Enum):
    MACHINE = "machine"
    DEPARTMENT = "department"
    COMPANY = "company"


class MessageType(Enum):
    PM = "PM"
    AI = "AI"







class Constance:
    app_name = 'msg'
    app_prefix = 'msg'
    scope = 2.00  # in kilometer
    pass_key = 'Mess@geSErV!ce7008'
