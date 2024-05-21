from mongoengine import Document, fields, connect

connect("applysias")


# Define the Report document
class Report(Document):
    date = fields.StringField(required=True)  # Store date as string
    time = fields.StringField(required=True)  # Store time as string
    movement = fields.FloatField(required=True)
    applysia = fields.IntField(required=True)
    trail_points = fields.ListField(fields.DictField(), required=True)
