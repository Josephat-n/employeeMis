from flask import render_template
from . import main
from .. import db
from ..models import Blog


@main.route('/')
def index():
   """
   Fetch the employees and details from the bd.
   """
   employees = Employee.query.all()
   print(employees)
   return render_template('index.html', employees = employees)