from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, ValidationError, PasswordField
from wtforms import validators, ValidationError
from .models import User

class SignupForm(FlaskForm):
    firstname = StringField("First name", validators=[validators.DataRequired("Please enter your first name.")])
    lastname = StringField("Last name", validators=[validators.DataRequired("Please enter your last name.")])
    email = StringField("Email", validators=[validators.DataRequired("Please enter your email address."), validators.Email("Please enter a valid email address.")])
    password = PasswordField('Password', validators=[validators.DataRequired("Please enter a password.")])
    phone_number = StringField("Phone number")
    gender = StringField("Gender")
    address = StringField("Address")
    city = StringField("City")
    country = StringField("Country")
    submit = SubmitField("Create account")

def __init__(self, *args, **kwargs):
    FlaskForm.__init__(self, *args, **kwargs)

def validate(self):
    if not FlaskForm.validate(self):
        return False
    user = User.query.filter_by(email=self.email.data.lower()).first()
    if user:
        self.email.errors.append("That email is already taken")
        return False
    else:
        return True

class SigninForm(FlaskForm):
    email = StringField("Email", validators=[validators.DataRequired("Please enter your email address."), validators.Email("Please enter a valid email address.")])
    password = PasswordField('Password', validators=[validators.DataRequired("Please enter a password.")])
    submit = SubmitField("Sign In")

    def __init__(self, *args, **kwargs):
        super(SigninForm, self).__init__(*args, **kwargs)

    def validate(self):
        if not super(SigninForm, self).validate():
            return False

        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user and user.check_password(self.password.data):
            return True
        else:
            self.email.errors.append("Invalid e-mail or password")
            return False

class FeedbackForm(FlaskForm):
    name = StringField("Name", validators=[validators.DataRequired("Please enter your name.")], description="Name")
    email = StringField("Email", validators=[validators.DataRequired("Please enter your email address."), validators.Email("Please enter a valid email address.")], description="Email")
    subject = StringField("Subject", validators=[validators.DataRequired("Please enter the subject.")], description="Subject")
    comment = StringField("Comment", validators=[validators.DataRequired("Please enter your comment.")], description="Comment")
    submit = SubmitField("Send Message")

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)

class SubmitArt(FlaskForm):
    name = StringField("Name", validators=[validators.DataRequired("Please enter the painting's title.")], description="Painting's title")
    location = StringField("Location", validators=[validators.DataRequired("Please enter the file location.")], description="Painting's location")
    artist_id = StringField("Artist_id", validators=[validators.DataRequired("Please enter the artist_id.")], description="Artist_id")
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
