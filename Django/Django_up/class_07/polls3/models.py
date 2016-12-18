from mongoengine import *

class Poem(Document):
    meta = {
        'collection':'poem_data'
    }
    poem_id = SequenceField(required=True, primary_key=True)
    author = StringField()
    title = StringField()