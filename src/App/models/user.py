from neomodel import StructuredNode, UniqueIdProperty, RelationshipTo, ZeroOrMore
from App.models.option import AnswerRel


class User(StructuredNode):
    user_id = UniqueIdProperty()
    answers = RelationshipTo('App.models.Option', 'ANSWERED_TO', cardinality=ZeroOrMore, model=AnswerRel)
