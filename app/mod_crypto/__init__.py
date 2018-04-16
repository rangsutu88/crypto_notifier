from flask import Blueprint

crypto = Blueprint(name="notifications", url_prefix="/crypto", static_folder="static", 
                template_folder="templates")

from . import views
