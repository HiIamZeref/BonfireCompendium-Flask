from marshmallow import Schema, fields

class PlatformSchema(Schema):
    '''
    Schema for Platform model.
    '''
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)