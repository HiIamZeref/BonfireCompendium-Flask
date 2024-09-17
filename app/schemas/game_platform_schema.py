from marshmallow import Schema, fields
from app.schemas.game_schema import GameSchema
from app.schemas.platform_schema import PlatformSchema

class GamePlatformSchema(Schema):
    game = fields.Nested(lambda: GameSchema(only=('id', 'title')))
    platform = fields.Nested(lambda: PlatformSchema(only=('id', 'name')))


class CreateOrDeleteGamePlatform(Schema):
    game_id = fields.Integer()
    platform_id = fields.Integer()