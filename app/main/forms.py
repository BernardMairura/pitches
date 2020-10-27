from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField,
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Title',validators=[Required()])
    review = TextAreaField("What is your comment?", validators=[Required()])
    submit = SubmitField('Submit')



class Comment(FlaskForm):
    description = TextAreaField('Add comment',validators=[Required()])
    submit = SubmitField()

class Upvote(FlaskForm):
	submit = SubmitField()


class Downvote(FlaskForm):
	submit = SubmitField()