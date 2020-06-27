from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class EmployeeForm(FlaskForm):
  name = StringField('Employee name',validators=[Required()])
  phone = StringField('Phone number',validators=[Required()])
  date_of_birth = StringField('Date of birth',validators=[Required()])
  position = StringField('position of empoloyee',validators=[Required()])
  duties = TextAreaField('Your Comment',validators=[Required()])
  
  submit = SubmitField('Submit')