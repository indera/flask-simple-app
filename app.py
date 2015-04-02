from flask import Flask
from flask import flash, request, redirect, url_for, render_template

from wtforms import Form, BooleanField, TextField, PasswordField, RadioField
from wtforms import validators 
 
SECRET_KEY = 'secret'
 
app = Flask(__name__)
app.config.from_object(__name__)

class LoginForm(Form):
    username    = TextField('Username', [validators.Length(min=4, max=25)])
    password    = PasswordField('Password', [validators.Required()])
 

class RegistrationForm(Form):
    username    = TextField('Username', [validators.Length(min=4, max=25)])
    email       = TextField('Email Address', [validators.Length(min=6, max=35)])
    password    = PasswordField('New Password', [
                    validators.Required(),
                    validators.EqualTo('confirm', message='Passwords must match')
                    ])
    confirm     = PasswordField('Repeat Password')
    """
    account_type= RadioField('Account type:',
                    choices=[
                        ('1', 'Admin'),
                        ('2', 'User'),
                        ('3', 'Tech Support'),
                        ]
                    )
    """
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])
 
 
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST','GET'])
def register():
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():
        user = (form.username.data, form.email.data,
                form.password.data)
        print user
        flash('Thanks for registering {}'.format(form.username.data), 'error')
        return redirect(url_for('index'))

    return render_template('register.html',form=form)
 

@app.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = (form.username.data, form.password.data)
        print user
        flash('Welcome {}'.format(user), 'error')
        return redirect(url_for('index'))
 
    return render_template('login.html',form=form)

if __name__ == '__main__':
    app.run(port=5002, debug=True)
