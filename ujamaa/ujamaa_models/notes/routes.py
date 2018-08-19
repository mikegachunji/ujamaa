from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)

notes = Blueprint('notes', __name__)