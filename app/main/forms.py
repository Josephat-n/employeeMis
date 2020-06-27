from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class EmployeeForm(FlaskForm):
  name = StringField('Employee name',validators=[Required()])
  phone = StringField('Phone number',validators=[Required()])
  date_of_birth = StringField('Date of birth',validators=[Required()])
  position = StringField('Position of empoloyee',validators=[Required()])
  duties = TextAreaField('Duties of the employee',validators=[Required()])
  earning = StringField('Salary of Employee',validators=[Required()])
  
  submit = SubmitField('Submit')