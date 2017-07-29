from neomodel import StructuredNode, UniqueIdProperty, StringProperty, RelationshipFrom, OneOrMore


class Question(StructuredNode):
    question_id = UniqueIdProperty()
    title = StringProperty(required=True)
    options = RelationshipFrom('App.models.Option', 'FOR_QUESTION', cardinality=OneOrMore)
