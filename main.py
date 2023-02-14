import os

from flask import Flask, render_template, url_for, flash
from flask_bootstrap import Bootstrap
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

from form import Form

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'abc')

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', "sqlite:///inventory.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CONFIGURE TABLE
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    fatherName = db.Column(db.String(100))
    address = db.Column(db.String(200))
    phoneNum = db.Column(db.String(10))
    email = db.Column(db.String(100), unique=True)
    aadhaar = db.Column(db.String(12))
    panNum = db.Column(db.String(100))
    bankName = db.Column(db.String(100))
    bankAccNum = db.Column(db.String(100), unique=True)
    bankIfscCode = db.Column(db.String(100))
    bankBranch = db.Column(db.String(100))
    doAbleLand = db.Column(db.String(100))
    mainCrops = db.Column(db.String(100))
    cattleCount = db.Column(db.String(100))
    enrollmentCount = db.Column(db.String(100))
    date = db.Column(db.String(100))


db.create_all()


@app.route('/', methods=["GET", "POST"])
def index():
    form = Form()

    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            fatherName=form.fatherName.data,
            address=form.address.data,
            phoneNum=form.phoneNum.data,
            email=form.email.data,
            aadhaar=form.aadhaar.data,
            panNum=form.panNum.data,
            bankName=form.bankName.data,
            bankAccNum=form.bankAccNum.data,
            bankIfscCode=form.bankIfscCode.data,
            bankBranch=form.bankBranch.data,
            doAbleLand=form.doAbleLand.data,
            mainCrops=form.mainCrops.data,
            cattleCount=form.cattleCount.data,
            enrollmentCount=form.enrollmentCount.data,
            date=form.date.data,
        )

        db.session.add(user)
        db.session.commit()
        flash("User details saved!")
        return redirect(url_for("index"))

    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
