from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField("First Name", validators=[DataRequired("Please Enter Your First Name.")])
    last_name = StringField("Last Name", validators=[DataRequired("Please Enter Your Last Name.")])
    email = StringField("Email", validators=[DataRequired("Please Enter Your Email Address."), Email("Please Enter Your Email Address.")])
    password = PasswordField("Password", validators=[DataRequired("Please Enter Your Password."), Length(min=6, message="Passwords Must Be 6 Characters or More.")])
    submit = SubmitField("Sign Up")

class LoginForm(Form):
    email = StringField("Email", validators=[DataRequired("Please Enter Your Email Address."), Email("Please Enter Your Email Address")])
    password = PasswordField("Password", validators=[DataRequired("Please Enter a Password.")])
    submit = SubmitField("Sign in")