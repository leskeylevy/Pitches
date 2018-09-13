from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import StringField, TextAreaField, SubmitField


class PitchForm(FlaskForm):
    title = StringField('Pitch title', validators=[Required()])
    content = TextAreaField('Pitch')
    submit = SubmitField('Submit')


class Test(FlaskForm):
    comment = TextAreaField('comment', validators=[Required()])
    # content = TextAreaField('Pitch')
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = StringField('Title', validators=[Required])
    submit = SubmitField('Submit')
