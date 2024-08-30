from marshmallow import Schema, fields

class DeveloperSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)