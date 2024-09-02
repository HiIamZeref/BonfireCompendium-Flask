from marshmallow import Schema, fields

class GameStatusSchema(Schema):
    '''
    Schema for GameStatus model.
    '''
    id = fields.Integer(dump_only=True)
    name = fields.Str(required=True)
    