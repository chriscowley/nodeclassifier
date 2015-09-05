import datetime
from flask import url_for

from nodeclassifier import db


class Condition(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    conditionkey = db.StringField(verbose_name="Condition", required=True)
    conditionvalue = db.StringField(verbose_name="Condition", required=True)


class Rule(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    rulename = db.StringField(max_length=255, required=True)
    conditions = db.ListField(db.EmbeddedDocumentField('Condition'))

    def get_absolute_url(self):
        return url_for('rule', kwarg={"rulename": self.rulename})

    def __unicode__(self):
        return self.rulename

    meta = {
            'allow_inheritance': True,
            'indexes': ['-created_at', 'rulename'],
            'ordering': ['-created_at']
    }
