from marshmallow import Schema, fields, validate

class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

class AuthSchema(Schema):
    access_token = fields.Str()
    refresh_token = fields.Str()


