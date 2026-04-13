from flask import Flask, render_template
import os

app = Flask(__name__)

print("FICHIER PYTHON UTILISÉ :", __file__)
print("DOSSIER COURANT :", os.getcwd())
print("DOSSIER TEMPLATES :", app.template_folder)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    print("ROUTE HOME APPELÉE")
    return render_template('home.html', posts=posts, title='Home')

@app.route("/index")
def index():
    return render_template('index.html', posts=posts[0], title='Index')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
