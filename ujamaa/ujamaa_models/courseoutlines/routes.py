from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)

courseoutlines = Blueprint('courseoutlines', __name__)