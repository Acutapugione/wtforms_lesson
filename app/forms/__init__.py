from flask_wtf import FlaskForm
from wtforms import StringField, ColorField, SubmitField
from wtforms.validators import DataRequired



class MyForm(FlaskForm):
    name = StringField(validators=[DataRequired()], description="Vasya")
    picture_background = ColorField()
    ok = SubmitField()