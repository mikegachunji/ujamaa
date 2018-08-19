from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)

courses = Blueprint('courses', __name__)