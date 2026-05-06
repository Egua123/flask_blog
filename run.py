from flaskblog import app, db
from flaskblog.models import User, Post


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
