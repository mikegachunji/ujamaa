from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask import send_from_directory
from ujamaa_models import db, documents
from ujamaa_models.config import Config
from ujamaa_models.models import Post, Course, CourseOutline
from ujamaa_models.courseoutlines.forms import AddCourseOutlineForm
from flask_login import login_user, current_user, login_required, logout_user


courseoutlines = Blueprint('courseoutlines', __name__)

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'info')


@courseoutlines.route('/add/<course_id>', methods=['GET', 'POST'])
def add_course_outline(course_id):
    # Cannot pass in 'request.form' to AddRecipeForm constructor, as this will cause 'request.files' to not be
    # sent to the form.  This will cause AddRecipeForm to not see the file data.
    # Flask-WTF handles passing form data to the form, so not parameters need to be included.
    form = AddCourseOutlineForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            filename = documents.save(request.files['document'])
            url = documents.url(filename)
            new_course_outline = CourseOutline(form.title.data, form.description.data, course_id, current_user.id, current_user.program_id, filename, url)
            db.session.add(new_course_outline)
            db.session.commit()
            flash('New Course Outline, {}, added!'.format(new_course_outline.title), 'success')
            return redirect(url_for('main.home'))
        else:
            flash_errors(form)
            flash('ERROR! Course Outline was not added.', 'error')
 
    return render_template('upload_course_outline.html', form=form, course_id=course_id)


@courseoutlines.route("/course_outline_profile/<course_id>")
def course_outline_profile(course_id):
	courseoutlines = CourseOutline.query.filter(CourseOutline.program_id == 1).filter(CourseOutline.course_id == 1).all()
	return render_template('course_outline_profile.html', courseoutlines=courseoutlines, course_id=course_id)



@courseoutlines.route('/course_outline/<course_outline_id>')
def course_outline_details(course_outline_id):
    courseoutline_with_course = db.session.query(CourseOutline).filter(CourseOutline.id == course_outline_id).first()
    return render_template('course_outline_details.html', courseoutline=courseoutline_with_course)


@courseoutlines.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(Config.UPLOADED_DOCUMENTS_DEST,
                               filename)


