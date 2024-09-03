from marshmallow import Schema, fields

class UserReviewSchema(Schema):
    '''
    Schema for UserReview model.
    '''
    id = fields.Integer(dump_only=True)
    game_id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)
    score = fields.Integer(required=True)
    status_id = fields.Integer(required=True)
    mastered = fields.Boolean()
    review = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    user = fields.Nested('UserSchema', only=('id', 'username'))
    game = fields.Nested('GameSchema', only=('id', 'name'))
    status = fields.Nested('GameStatusSchema', only=('id', 'name'))