from marshmallow import Schema, fields

class GamePlatformSchema(Schema):
    game_id = fields.Integer()
    platform_id = fields.Integer()