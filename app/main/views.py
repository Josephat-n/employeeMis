from flask import render_template
from . import main
from .. import db
from ..models import Employee
from .forms import EmployeeForm


@main.route('/')
def index():
   """
   Fetch the employees and details from the bd.
   """
   employees = Employee.query.all()
   print(employees)
   return render_template('index.html', employees = employees)

@main.route('/add_employee')
def addemp():
   """
   Add a new employee to the database
   """
   form = EmployeeForm()
   return render_template('addemp.html', addemp_form = form)
   