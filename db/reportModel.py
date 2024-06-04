from mongoengine import Document, fields, connect


# Define the Report document
class Report(Document):
    date = fields.StringField(required=True)  # Store date as string
    time = fields.DateTimeField(required=True)
    movement = fields.FloatField(required=True)
    applysia = fields.IntField(required=True)
    trail_points = fields.ListField(fields.DictField(), required=True)
    movement_every_five = fields.ListField(fields.FloatField(), required=True)