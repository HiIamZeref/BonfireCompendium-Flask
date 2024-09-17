from marshmallow import Schema, fields

class GameSchema(Schema):
    '''
    Schema for Game model.
    '''
    id = fields.Integer(dump_only=True)
    title = fields.Str(dump_only=True)
    description = fields.Str(dump_only=True)
    release_date = fields.Date(dump_only=True)
    genre = fields.Method("get_genre")
    developer = fields.Method("get_developer")
    publisher = fields.Method("get_publisher")
    cover_image = fields.Str()

    def get_genre(self, obj):
        return obj.genre.name
    
    def get_developer(self, obj):
        return obj.developer.name
    
    def get_publisher(self, obj):
        return obj.publisher.name


class CreateOrDeleteGameSchema(Schema):
    '''
    Schema for creating or deleting a Game object.
    '''
    id = fields.Integer(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    release_date = fields.Date(required=True)
    genre_id = fields.Integer(required=True)
    developer_id = fields.Integer(required=True)
    publisher_id = fields.Integer(required=True)
    cover_image = fields.Str()