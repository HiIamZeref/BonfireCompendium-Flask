from marshmallow import Schema, fields

class FollowerSchema(Schema):
    '''
    Schema for Follower model.
    '''
    id = fields.Integer(dump_only=True)
    user_id = fields.Integer(required=True)
    follower_id = fields.Integer(required=True)