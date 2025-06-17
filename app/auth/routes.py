from flask import render_template, redirect, url_for, flash  # noqa: F401
from . import bp

@bp.route('/login')
def login():
    return render_template('auth/login.html', title='Sign In')

@bp.route('/logout')
def logout():
    return redirect(url_for('main.index')) 
