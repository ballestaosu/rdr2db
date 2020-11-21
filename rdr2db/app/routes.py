from flask import render_template, flash, redirect, url_for, request, redirect, Flask
from flask_bootstrap import Bootstrap
from db_connector.db_connector import connect_to_database, execute_query
from app.forms import LoginForm

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'andre'}
    pages = [
        {
            'page': {'header': 'PAGE'},
            'description': 'DESCRIPTION'
        },
        {
            'page': {'header': 'Users'},
            'description': 'Add users'
        },
        {
            'page': {'header': 'Horses'},
            'description': 'Browse the horses'
        }
    ]
    return render_template('index.html', title='Home', user=user, pages=pages)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/users')
def users():
    return render_template('users.html', title='Users - RDR2 DB')


@app.route('/characters')
def characters():
    return render_template('characters.html', title='Characters - RDR2 DB')


@app.route('/weapons')
def weapons():
    return render_template('weapons.html', title='Weapons - RDR2 DB')


@app.route('/horses')
def horses():
    user = {'username': 'andre'}
    return render_template('horses.html', title='Horses - RDR2 DB', user=user)


@app.route('/locations')
def locations():
    return render_template('locations.html', title=' Locations - RDR2 DB')


@app.route('/leg_animals')
def leg_animals():
    return render_template('leg_animals.html', title=' L. Animals - RDR2 DB')
