from flask import render_template
from . import auth

@auth.route('/registerUser')
def registerUser():
	return render_template('auth/register.html')