from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from models import db
from models import Actor
from schemas import actor_schema, actors_schema

# Create a "Blueprint", or module
# We can insert this into our Flask app
actors_router = Blueprint('actors', __name__, url_prefix='/actors')


# GET requests to the collection return
# a list of all actors in the database
@actors_router.get('/')
def read_all_actors():
    actors = Actor.query.all()               # Get all the actors
    return actors_schema.dump(actors)  # Serialize the actors


# GET requests to a specific document in
# the collection return a single actor
@actors_router.get('/<actor_id>')
def read_actor(actor_id):
    actor = Actor.query.get(actor_id)  # Get the actor by id
    return actor_schema.dump(actor)    # Serialize the actor


@actors_router.post('/')
def create_actor():
    actor_data = request.json          # Get the parsed request body

    try:
        actor_schema.load(actor_data)  # Validate against the schema
    except ValidationError as err:
        return jsonify(err.messages), 400

    actor = Actor(**actor_data)        # Create a new actor model
    db.session.add(actor)              # Insert the record
    db.session.commit()                # Update the database

    return actor_schema.dump(actor)    # Serialize the created actor
