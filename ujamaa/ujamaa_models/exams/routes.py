from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)

exams = Blueprint('exams', __name__)