from flask import Blueprint
from routes.actors import actors_router

# Create a routes module to be registered in our app
router = Blueprint('api', __name__, url_prefix='/api')

# Register our nested routes
router.register_blueprint(actors_router)
