from flask import render_template
from . import auth
from .forms import RegisterUserForm

@auth.route('/registerUser')
def registerUser():
	registration_form = RegisterUserForm()
	return render_template('auth/register.html', registration_form = registration_form)