from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired


class Form(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    fatherName = StringField("Father's Name", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    phoneNum = StringField("Number", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    aadhaar = StringField("Aadhar", validators=[DataRequired()])
    panNum = StringField("Pan Number", validators=[DataRequired()])
    bankName = StringField("Bank Name", validators=[DataRequired()])
    bankAccNum = StringField("Bank Account Number", validators=[DataRequired()])
    bankIfscCode = StringField("Bank IFSC Code", validators=[DataRequired()])
    bankBranch = StringField("Bank Branch", validators=[DataRequired()])
    doAbleLand = StringField("Doable Land", validators=[DataRequired()])
    mainCrops = StringField("Main Crops")
    cattleCount = IntegerField("Cattle's Count", validators=[DataRequired()])
    enrollmentCount = StringField('Enrollment Count', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField("Submit")
