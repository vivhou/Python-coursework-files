from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about_author')
def about():
 	return render_template('about_author.html')

@app.route('/results')
def results():
 	return render_template('results.html')

@app.route('/methodology')
def methodology():
 	return render_template('methodology.html')

@app.route('/project_description')
def project_description():
 	return render_template('project_description.html')

@app.route('/research_question')
def research_question():
 	return render_template('research_question.html')
if __name__ == '__main__':
	app.run(debug=True)