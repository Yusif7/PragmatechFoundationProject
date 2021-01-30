
from app import app,db

from blog.routes import blogs

app.register_blueprint(blogs)