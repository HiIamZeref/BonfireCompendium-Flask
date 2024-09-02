from marshmallow import Schema, fields

class GameSchema(Schema):
    '''
    Schema for Game model.
    '''
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    release_date = fields.Date(required=True)
    genre_id = fields.Integer(required=True)
    developer_id = fields.Integer(required=True)
    publisher_id = fields.Integer(required=True)
    cover_image = fields.Str()