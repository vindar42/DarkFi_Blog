from flask import Flask, render_template, url_for, redirect, request
from markdown2 import markdown
from jinja2 import Environment, PackageLoader
import os
import glob
import pypandoc
from datetime import datetime 

app = Flask(__name__)

posts = {}
for markdown_post in os.listdir('templates'):
  if markdown_post.endswith('md'):
   file_path = os.path.join('templates', markdown_post)

   with open(file_path, 'r') as file:
     posts[markdown_post] = markdown(file.read(), extras=['metadata'])

env = Environment(loader=PackageLoader('app', 'templates'))
test_template = env.get_template('index.html')
posts_metadata = [posts[post].metadata for post in posts]


url = []
date = []

for data in posts_metadata:
 url.append(data['url'])
 my_date = datetime.strptime(data['list1'], "%Y.%m.%d").date()
 date.append(my_date)
 li = list(zip(date, url))
 print(li)
#with open('templates/history1.md', 'r') as f:
# text = f.read()
# html = pandoc --toc --mathjax -f markdown -t html history1.md -o history1.html
#with open('templates/history1.html','w') as f:
# f.write(html)

@app.route('/')
def test():
 csslink = url_for('static', filename='css/main.css')
 return render_template('index.html', posts=posts_metadata, csslink=csslink)

@app.route('/featured')
def featured():
 csslink = url_for('static', filename='css/main.css')
 return render_template('featured-article.html',csslink=csslink)

@app.route('/archive')
def archive():
 csslink = url_for('static', filename='css/main.css')
 return render_template('archive.html',csslink=csslink,posts=posts_metadata)

@app.route('/history_archive')
def history_archive():
 csslink = url_for('static', filename='css/main.css')
 return render_template('history_archive.html',csslink=csslink,posts=posts_metadata)

@app.route('/insight_archive')
def insight_archive():
 csslink = url_for('static', filename='css/main.css')
 return render_template('insight_archive.html',csslink=csslink,posts=posts_metadata)

@app.route('/technology_archive')
def technology_archive():
 csslink = url_for('static', filename='css/main.css')
 return render_template('technology_archive.html',csslink=csslink,posts=posts_metadata)

@app.route('/market_archive')
def market_archive():
 csslink = url_for('static', filename='css/main.css')
 return render_template('market_archive.html',csslink=csslink,posts=posts_metadata)

@app.route('/xenopoetisc_archive')
def xenopoetisc_archive():
 csslink = url_for('static', filename='css/main.css')
 return render_template('xenopoetisc_archive.html',csslink=csslink,posts=posts_metadata)


@app.route('/history1')
def history1():
 csslink = url_for('static', filename='css/main.css')
 return render_template('history1.html',csslink=csslink, posts=posts_metadata)

@app.route('/history2')
def history2():
 csslink = url_for('static', filename='css/main.css')
 return render_template('history2.html',csslink=csslink,posts=posts_metadata)

@app.route('/history3')
def history3():
 csslink = url_for('static', filename='css/main.css')
 return render_template('history3.html',csslink=csslink,posts=posts_metadata)

@app.route('/history4')
def history4():
 csslink = url_for('static', filename='css/main.css')
 return render_template('history4.html',csslink=csslink,posts=posts_metadata)


@app.route('/insight')
def insight():
 csslink = url_for('static', filename='css/main.css')
 return render_template('insight1.md',csslink=csslink,posts=posts_metadata)

if __name__ == '__app__':
        app.run()

