from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///your_db.db"
app.secret_key = "your secret key"
db.init_app(app)

class Your_Table(db.Model):
    your_column = db.Column(db.Integer, primary_key=True)

    def __init__(self, your_column):
        self.your_column = your_column


@app.route('/')
def dashboard():
    return render_template('dashboard.html', things=Your_Table.query.all())


@app.route('/add_thing', methods=["GET", "POST"])
def add_thing():
    thing = request.form.get('thing')

    if request.method == "POST":
        if not thing:
            flash("Please, fill out all fields")
        else:
            variable = Your_Table(thing)
            db.session.add(variable)
            db.session.commit()
            return redirect(url_for('dashboard'))
    
    return render_template('add_thing.html')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)