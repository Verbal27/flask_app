from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:121212io@localhost/flaskProject'
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://ajvovrjkftyuqc:6234f2d28dd75cf6052f4f147a414408fde93bf8d7e46442c5719bfa2a095b88@ec2-54-228-9-90.eu-west-1.compute.amazonaws.com:5432/d2h24og6slf9i4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(30))
    comment = db.Column(db.String(150))


@app.route('/')
def index():
    res = Comments.query.all()
    return render_template('index.html', res=res)


@app.route('/content')
def main():
    return render_template('main.html')


@app.route('/process', methods=['POST'])
def process():
    author = request.form['author']
    comment = request.form['comment']
    data = Comments(author=author, comment=comment)
    db.session.add(data)
    db.session.commit()

    return redirect(url_for('index'))
