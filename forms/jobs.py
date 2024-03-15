from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job = StringField('Job', validators=[DataRequired()])
    work_size = StringField("Work hours", validators=[DataRequired()])
    collaborators = StringField('Collaborators')
    start_date = DateField("Start Date", validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
    is_finished = BooleanField("Is finished")
    submit = SubmitField('Submit')
