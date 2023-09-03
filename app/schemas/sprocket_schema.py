from marshmallow import Schema, fields

class SprocketSchema(Schema):
    teeth = fields.Int(required=True)
    pitch_diameter = fields.Float(required=True)
    outside_diameter = fields.Float(required=True)
    pitch = fields.Float(required=True)