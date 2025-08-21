from flask_marshmallow import Marshmallow
from models import Actor

# Initialise Marshmallow
ma = Marshmallow()


# Auto-generate a schema for Actor models
# We can use this to serialize and validate actor data
class ActorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Actor


# Instantiate the schema for both a single actor and many actors
actor_schema = ActorSchema()
actors_schema = ActorSchema(many=True)
