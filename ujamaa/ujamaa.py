from flask import Flask, render_template, url_for
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
	{
		'author': 'Michael Gachunji',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'June 26 2018'
	},
		{
		'author': 'Nahashon Njenga',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'June 27 2018'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title='About')



if __name__ == "__main__":
	app.run(debug=True)