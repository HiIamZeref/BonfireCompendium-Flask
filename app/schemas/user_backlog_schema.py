from marshmallow import Schema, fields
from app.schemas.game_schema import GameSchema


class UserBacklogSchema(Schema):
    '''
    Schema for UserBacklog model.
    '''
    id = fields.Integer(dump_only=True)
    game = fields.Nested(lambda: GameSchema(only=('id', 'title')))
    created_at = fields.DateTime(dump_only=True)

    


class CreateOrDeleteUserBacklogSchema(Schema):
    '''
    Schema for creating or deleting a UserBacklog object.
    '''
    id = fields.Integer(dump_only=True)
    game_id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    