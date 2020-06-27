from flask import render_template, redirect, url_for, flash
from . import main
from .. import db
from ..models import Employee
from .forms import EmployeeForm


@main.route('/')
def index():
   """
   This is the default landing page, containing the welcome message.
   """
   
   return render_template('index.html')

@main.route('/add_employee', methods = ['GET','POST'])
def addemp():
   """
   Add a new employee to the database
   """
   form = EmployeeForm()
   new_employee = Employee()
   
   #functionality to save form data
   if form.validate_on_submit():
      new_employee.name = form.name.data
      new_employee.phoneno = form.phone.data
      new_employee.birthdate = form.date_of_birth.data
      new_employee.position = form.position.data
      new_employee.duties = form.duties.data
      new_employee.earning = form.earning.data
      
      db.session.add(new_employee)
      db.session.commit()
      
      flash('New Employee added successfully!')   
      return redirect(url_for('.addemp'))
   
   
   return render_template('addemp.html', addemp_form = form)

@main.route('/view_reports')
def reports():
   """
   View employees report. This includes fetching all the employees details from the bd.
   """
   employees = Employee.query.all()
   print(employees)
   
   return render_template('report.html', employees = employees)
      
   