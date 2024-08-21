from marshmallow import Schema, fields
from app import bcrypt
from models import User

class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    bio = fields.Str()
    photo = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(**validated_data, password=hashed_password)
        return user