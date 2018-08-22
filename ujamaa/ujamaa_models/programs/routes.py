from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from ujamaa_models.models import Post, Course

programs = Blueprint('programs', __name__)


@programs.route("/it_index")
def it_index():
	page = request.args.get('page', 1, type=int)
	posts = Post.query.filter(Post.program_id == 1).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('it_home.html', posts=posts)

@programs.route("/it_profile")
def it_profile():
	return render_template('it_profile.html')

@programs.route("/business_profile")
def business_profile():
	return render_template('business_profile.html')

@programs.route("/economics_profile")
def economics_profile():
	return render_template('economics_profile.html')

@programs.route("/first_year_economics_profile")
def first_year_economics_profile():
	courses = Course.query.filter(Course.program_id == 3).filter(Course.year == 1).all()
	print (courses)
	return render_template('first_year_economics_profile.html', courses=courses)

@programs.route("/first_year_it_profile")
def first_year_it_profile():
	courses = Course.query.filter(Course.program_id == 1).filter(Course.year == 1).all()
	print (courses)
	return render_template('first_year_it_profile.html', courses=courses)

@programs.route("/first_year_business_profile")
def first_year_business_profile():
	courses = Course.query.filter(Course.program_id == 2).filter(Course.year == 1).all()
	print (courses)
	return render_template('first_year_business_profile.html', courses=courses)

@programs.route("/second_year_economics_profile")
def second_year_economics_profile():
	courses = Course.query.filter(Course.program_id == 3).filter(Course.year == 2).all()
	print (courses)
	return render_template('second_year_economics_profile.html', courses=courses)

@programs.route("/second_year_it_profile")
def second_year_it_profile():
	courses = Course.query.filter(Course.program_id == 1).filter(Course.year == 2).all()
	print (courses)
	return render_template('second_year_it_profile.html', courses=courses)

@programs.route("/second_year_business_profile")
def second_year_business_profile():
	courses = Course.query.filter(Course.program_id == 2).filter(Course.year == 2).all()
	print (courses)
	return render_template('second_year_business_profile.html', courses=courses)

@programs.route("/third_year_economics_profile")
def third_year_economics_profile():
	courses = Course.query.filter(Course.program_id == 3).filter(Course.year == 3).all()
	print (courses)
	return render_template('third_year_economics_profile.html', courses=courses)

@programs.route("/third_year_it_profile")
def third_year_it_profile():
	courses = Course.query.filter(Course.program_id == 1).filter(Course.year == 3).all()
	print (courses)
	return render_template('third_year_it_profile.html', courses=courses)

@programs.route("/third_year_business_profile")
def third_year_business_profile():
	courses = Course.query.filter(Course.program_id == 2).filter(Course.year == 3).all()
	print (courses)
	return render_template('third_year_business_profile.html', courses=courses)

@programs.route("/fourth_year_economics_profile")
def fourth_year_economics_profile():
	courses = Course.query.filter(Course.program_id == 3).filter(Course.year == 4).all()
	print (courses)
	return render_template('fourth_year_economics_profile.html', courses=courses)

@programs.route("/fourth_year_it_profile")
def fourth_year_it_profile():
	courses = Course.query.filter(Course.program_id == 1).filter(Course.year == 4).all()
	print (courses)
	return render_template('fourth_year_it_profile.html', courses=courses)

@programs.route("/fourth_year_business_profile")
def fourth_year_business_profile():
	courses = Course.query.filter(Course.program_id == 2).filter(Course.year == 4).all()
	print (courses)
	return render_template('fourth_year_business_profile.html', courses=courses)


@programs.route("/course_outline_profile/<course_id>")
def course_outline_profile(course_id):
	courseoutlines = CourseOutline.query.filter(CourseOutline.program_id == 1).filter(CourseOutline.course_id == 1).all()
	return render_template('course_outline_profile.html', courseoutlines=courseoutlines)


@programs.route("/first_year_it_course_profile/<course_id>")
def first_year_it_course_profile(course_id):
	return render_template('first_year_it_course_profile.html', course_id=course_id)


@programs.route("/second_year_it_course_profile/<course_id>")
def second_year_it_course_profile(course_id):
	return render_template('second_year_it_course_profile.html', course_id=course_id)


@programs.route("/third_year_it_course_profile/<course_id>")
def third_year_it_course_profile(course_id):
	return render_template('third_year_it_course_profile.html', course_id=course_id)


@programs.route("/fourth_year_it_course_profile/<course_id>")
def fourth_year_it_course_profile(course_id):
	return render_template('fourth_year_it_course_profile.html', course_id=course_id)


@programs.route("/first_year_business_course_profile/<course_id>")
def first_year_business_course_profile(course_id):
	return render_template('first_year_business_course_profile.html', course_id=course_id)


@programs.route("/second_year_business_course_profile/<course_id>")
def second_year_business_course_profile(course_id):
	return render_template('second_year_business_course_profile.html', course_id=course_id)


@programs.route("/third_year_business_course_profile/<course_id>")
def third_year_business_course_profile(course_id):
	return render_template('third_year_business_course_profile.html', course_id=course_id)


@programs.route("/fourth_year_business_course_profile/<course_id>")
def fourth_year_business_course_profile(course_id):
	return render_template('fourth_year_business_course_profile.html', course_id=course_id)


@programs.route("/first_year_economics_course_profile/<course_id>")
def first_year_economics_course_profile(course_id):
	return render_template('first_year_economics_course_profile.html', course_id=course_id)


@programs.route("/second_year_economics_course_profile/<course_id>")
def second_year_economics_course_profile(course_id):
	return render_template('second_year_economics_course_profile.html', course_id=course_id)


@programs.route("/third_year_economics_course_profile/<course_id>")
def third_year_economics_course_profile(course_id):
	return render_template('third_year_economics_course_profile.html', course_id=course_id)


@programs.route("/fourth_year_economics_course_profile/<course_id>")
def fourth_year_economics_course_profile(course_id):
	return render_template('fourth_year_economics_course_profile.html', course_id=course_id)


@programs.route("/business_index")
def business_index():
	page = request.args.get('page', 1, type=int)
	posts = Post.query.filter(Post.program_id == 2).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('business_home.html', posts=posts)


@programs.route("/economics_index")
def economics_index():
	page = request.args.get('page', 1, type=int)
	posts = Post.query.filter(Post.program_id == 3).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('economics_home.html', posts=posts)