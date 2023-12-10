from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegisterForm(FlaskForm):
    """Register Form"""
    username =  StringField('Username', validators=[DataRequired(), Length(1,64)])
    email =  StringField('Email', validators=[DataRequired(), Length(1,64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField('Register')

class ProductForm(FlaskForm):
    """Product Form"""
    product_name =  StringField('Product Name', validators=[DataRequired(), Length(1,64)])
    product_description =  TextAreaField('Product Description', validators=[DataRequired()])
    stock_available = SelectField('Stock Available', choices=[
        (1, 1), (2, 2), (4, 4)
    ])
    submit = SubmitField('Add Product')