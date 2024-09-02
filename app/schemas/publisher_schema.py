from marshmallow import Schema, fields

class PublisherSchema(Schema):
    '''
    Schema for Publisher model.
    '''
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)