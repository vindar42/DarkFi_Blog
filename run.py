from flask import Flask, render_template
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)
@app.route('/')

#file_loader = FileSystemLoader('templates')
#env = Environment(loader=file_loader)
def template_test():

	return template ('child.html')
if __name__ == '__main__':
	app.run(debug=True)
