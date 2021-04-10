from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import StringField, PasswordField, IntegerField, TextField, FloatField, FileField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask.helpers import send_from_directory

class PropertyForm(FlaskForm):
    title = TextField("Property Title", validators =[DataRequired()])
    description = TextAreaField("Description", validators =[DataRequired()])
    bedroom = TextField("No. of Rooms", validators =[DataRequired()])
    bathroom = TextField("No. of Bathrooms", validators =[DataRequired()])
    price = TextField("Price", validators=[DataRequired()])
    ptype= SelectField("Property Type", choices=[('House','House'),('Apartment','Apartment')] ,validators = [DataRequired()])
    location = TextField("Location", validators = [DataRequired()]) 
    photo = FileField("Photo", validators = [FileAllowed(['jpg','png'],"Please use only jpg or png images!"), FileRequired()])

