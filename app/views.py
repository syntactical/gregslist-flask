from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Paul Toadman'}
	listings = [
		{
			'title': "FAKE CHRISTMAS TREES",
			'description': "50,000 fake Christmas trees. All must go by Friday. Local pickup only"
		},
		{
			'title': "Rodeo Equipment",
			'description': "Rodeo equipment, all must go. Local pickup only"
		}
	]
	return render_template('index.html', title="Hello", user=user, listings=listings)

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' %
			(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html',
							title="Sign In",
							form=form,
							providers=app.config['OPENID_PROVIDERS'])
