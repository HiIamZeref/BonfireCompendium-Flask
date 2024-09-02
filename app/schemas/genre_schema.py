from marshmallow import Schema, fields

class GenreSchema(Schema):
    '''
    Schema for Genre model.
    '''
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)