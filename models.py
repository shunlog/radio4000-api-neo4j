from neomodel import (StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, RelationshipFrom,
                      DateTimeFormatProperty, FloatProperty, StructuredRel,
                      BooleanProperty, DateProperty)

class TagRel(StructuredRel):
    channel = StringProperty(required=True)

class Track(StructuredNode):
    uid = UniqueIdProperty()
    url = StringProperty(unique_index=True, required=True)
    title = StringProperty()
    body = StringProperty()
    media_not_available = BooleanProperty(default=False)
    created = DateProperty()
    discogs_url = StringProperty()
    tags = RelationshipTo('Tag', 'TAGGED', model=TagRel)

class Channel(StructuredNode):
    uid = UniqueIdProperty()
    slug = StringProperty(unique_index=True, required=True)
    title = StringProperty()
    body = StringProperty()
    created = DateProperty()
    image = StringProperty()
    is_featured = BooleanProperty(default=False)
    link = StringProperty()
    updated = DateProperty()
    follows = RelationshipTo('Channel', 'FOLLOWS')
    likes = RelationshipTo('Track', 'LIKES')

class Tag(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True, required=True)
