import datetime
import json


def data_converter(o):
    if isinstance(o, datetime):
        return o.__str__()
    else:
        return o.__dict__


class JsonSerializable(object):

    def to_json(self):
        return json.dumps(self.to_dict(), default=data_converter)

    def __repr__(self):
        return self.to_json()

    def to_dict(self):
        return self.__dict__


class Model(JsonSerializable):
    def update_obj(self, data: dict):
        """

        :type data: dict
        """
        for key in data.keys():
            setattr(self, key, data[key]) if hasattr(self, key) else None


class CreateApModel(Model):
    def __init__(self, wiface, bridge, ssid, password, virt_prefix, channel=1, wpa_version='1+2', timeout=30):
        self.wiface = wiface
        self.bridge = bridge
        self.ssid = ssid
        self.password = password
        self.virt_prefix = virt_prefix
        self.channel = channel
        self.wpa_version = wpa_version
        self.timeout = timeout

    @staticmethod
    def from_dict(data):
        return CreateApModel(**data)
