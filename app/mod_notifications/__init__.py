from flask import Blueprint

notifications = Blueprint(name="notifications", url_prefix="/notifications", static_folder="static", 
                template_folder="templates")

from . import views
