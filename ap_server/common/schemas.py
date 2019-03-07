from marshmallow import Schema, fields, post_load

from ap_server.common.models import CreateApModel


class CreateApSchema(Schema):
    wiface = fields.Str(required=True)
    bridge = fields.Str(required=True)
    ssid = fields.Str(required=True)
    virt_prefix = fields.Str(required=True)
    password = fields.Str()
    freq_band = fields.Str(default="2.4")
    channel = fields.Str(default=1)
    wpa_version = fields.Str(default="1+2")
    timeout = fields.Int(default=20)

    @post_load
    def make_slice(self, data):
        return CreateApModel(**data)
