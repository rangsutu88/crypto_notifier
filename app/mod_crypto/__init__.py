from flask import Blueprint

crypto = Blueprint(name="crypto", url_prefix="/crypto", static_folder="static",
                   template_folder="templates", import_name=__name__)

from . import views
