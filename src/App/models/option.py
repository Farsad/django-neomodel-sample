from neomodel import StructuredNode, StructuredRel, UniqueIdProperty, StringProperty, DateTimeProperty, \
    RelationshipFrom, RelationshipTo, One, ZeroOrMore
from datetime import datetime


class Option(StructuredNode):
    option_id = UniqueIdProperty()
    title = StringProperty(required=True)
    question = RelationshipTo('App.models.Question', 'FOR_QUESTION', cardinality=One)
    users = RelationshipFrom('App.models.User', 'ANSWERED_TO', cardinality=ZeroOrMore)


class AnswerRel(StructuredRel):
    answered_on = DateTimeProperty(default=lambda: datetime.utcnow())