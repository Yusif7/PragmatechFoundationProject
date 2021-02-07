
from app import app,db

from auth.routes import auth

app.register_blueprint(auth)

