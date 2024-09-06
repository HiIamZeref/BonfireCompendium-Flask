from marshmallow import Schema, fields

class FollowerSchema(Schema):
    '''
    Schema for Follower model.
    '''
    user = fields.Method("get_user_username")
    follower_username = fields.Method("get_follower_username")

    def get_user_username(self, obj):
        return obj.user.username
    
    def get_follower_username(self, obj):
        return obj.follower.username
    

class CreateOrDeleteFollowerSchema(Schema):
    '''
    Schema for creating a Follower object.
    '''
    user_id = fields.Integer(required=True)
    follower_id = fields.Integer(required=True)