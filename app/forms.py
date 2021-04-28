from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    """
    
    """
    
class OverviewForm(FlaskForm):
    """
    Represent the form for the account home page.

    Attributes
    ----------
    logout : SubmitField
        Button for user to log out.
    complete : BooleanField
        Checkbox for user to mark task as complete.
    """
    logout = SubmitField('Log out')
    complete = BooleanField('Mark as complete')
    createtask = SubmitField('Create Task')
    deletetask = SubmitField('Delete Task')

class NewTaskForm(FlaskForm):
    """
    Represents the form for creating a new task.

    Attributes
    ----------
    title : StringField
        Where users can type in the title of a new task. Data is required for this.
    description : StringField
        Where users can type in the description of a new task. Data is not required for this.
    create : SubmitField
        Button for user to finish creating new task.
    """
    title = StringField('Title', validators = [DataRequired()])
    description = StringField('Description')
    create = SubmitField('Create')
    date = StringField("Set Deadline (Optional) MM-DD-YYYY")
