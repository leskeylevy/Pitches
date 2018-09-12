from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import StringField,TextAreaField,SubmitField


class PitchForm(FlaskForm):
    title = StringField('Pitch title', validators=[Required()])
    content = TextAreaField('Pitch')
    submit = SubmitField('Submit')