
from app import app,db

from admin.routes import admin

app.register_blueprint(admin)