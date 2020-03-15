from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
<<<<<<< HEAD
from application.models import Users
from flask_login import current_user

class PostForm(FlaskForm):
    
    title = StringField('Title',
=======
from application.models import Users, Players, Stats
from flask_login import current_user
from wtforms.ext.sqlalchemy.fields import QuerySelectField

# class PostForm(FlaskForm):
    
#     title = StringField('Title',
#         validators = [
#             DataRequired(),
#             Length(min=2, max=100)
#         ]
#     )
#     content = TextAreaField('Content',
#         validators = [
#             DataRequired(),
#             Length(min=2, max=1000)
#         ]
#     )
#     submit = SubmitField('Post Content')
class PlayerForm(FlaskForm):
    
    player_name = StringField('Player Full Name',
>>>>>>> trials
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
<<<<<<< HEAD
    content = TextAreaField('Content',
        validators = [
            DataRequired(),
            Length(min=2, max=1000)
        ]
    )
    submit = SubmitField('Post Content')

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
=======
    player_age = StringField('Player Age',
        validators = [
            DataRequired(),
            Length(min=1, max=3)
        ]
    )
    player_team = StringField('Player Team',
>>>>>>> trials
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
<<<<<<< HEAD
    last_name = StringField('Last Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
=======
    submit = SubmitField('Add Player')

class StatsForm(FlaskForm):
    # user = current_user.id
    player_id = QuerySelectField(
        'Choose a Player',
        query_factory=lambda: Players.query.filter_by(id=current_user.id),
        allow_blank=False
    )
    
    goals = StringField('Goals',
        validators = [
            DataRequired(),
            Length(min=1, max=2)
        ]
    )
    assists = StringField('Assists',
        validators = [
            DataRequired(),
            Length(min=1, max=3)
        ]
    )
    chances = StringField('Chances',
        validators = [
            DataRequired(),
            Length(min=1, max=3)
        ]
    )

    shots = StringField('Shots',
        validators = [
            DataRequired(),
            Length(min=1, max=3)
        ]
    )
    minutes = StringField('Minutes Played',
        validators = [
            DataRequired(),
            Length(min=1, max=3)
        ]
    )
    date = DateField('Enter Date(dd-mm-yy)',
            format="%d-%m-%Y")
        
    
    submit = SubmitField('Add Stats')

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    last_name = StringField('Last Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
>>>>>>> trials
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email(message='Please Input a valid Email Address')
        ]
    )
    password = PasswordField('Password',
        validators = [
            DataRequired(message='Passwords can not be empty'), 
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password', message='Passwords must match')
        ]
    )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')


class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    last_name = StringField('Last Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')