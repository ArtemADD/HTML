from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job = StringField('Job Title', validators=[DataRequired()])
    team_leader = StringField('Team Leader id', validators=[DataRequired()])
    work_size = StringField("Work Size", validators=[DataRequired()])
    collaborators = StringField('Collaborators')
    category = SelectField('Hazard category', choices=[(1, ' Hazard 1'), (2, 'Hazard 2'), (3, 'Hazard 3'),
                                                       (4, 'Hazard 4'), (5, 'Hazard 5')])
    is_finished = BooleanField("Is job finished?")
    submit = SubmitField('Submit')
