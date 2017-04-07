from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import	DataRequired, Email, Length

class SignupForm(Form):
	first_name = StringField('First name', validators=[DataRequired("Please enter your firstname")])
	last_name = StringField('Last name', validators=[DataRequired("Please enter your lastname")])
	email = StringField('Email', validators=[DataRequired("Please enter your email"), Email('Please enter your email')])
	password = PasswordField('Password', validators=[DataRequired("Please enter your password"), Length(min=6, message="please must be 6 characters or more")])
	submit = SubmitField('Sign up')

class LoginForm(Form):
	email = StringField('Email', validators=[DataRequired("Please enter your email"), Email('Please enter your email')])
	password = PasswordField('Password', validators=[DataRequired('Please enter password'), Length(min=6, message="Please must be 6 characters or more")])
	submit = SubmitField('Sign In')