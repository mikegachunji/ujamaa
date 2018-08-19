from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from ujamaa_models import db
from ujamaa_models.models import University
from ujamaa_models.universities.forms import UniversityForm

universities = Blueprint('universities', __name__)


@universities.route("/university/new", methods=['GET', 'POST'])
@login_required
def new_university():
    form = UniversityForm()
    if form.validate_on_submit():
        university = University(title=form.title.data)
        db.session.add(university)
        db.session.commit()
        flash('New University created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_university.html', title='New University',
                           form=form, legend='New University')