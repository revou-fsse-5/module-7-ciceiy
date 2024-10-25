from flask import Blueprint, request, redirect, url_for, render_template, session
from flask_login import login_user, logout_user, login_required, current_user
from models.user_model import User
from connectors.db import Session

userBp = Blueprint('user', __name__)

@userBp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        with Session() as session_db:
            user = session_db.query(User).filter_by(email=email).first()
            if user and user.check_password(password):
                login_user(user)

                session['user_id'] = user.id
                session['role'] = user.role

                return redirect(url_for('home', name=user.username))
            else:
                return redirect(url_for('user.login', error='Wrong email or password'))
    return render_template('login.html')

@userBp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@userBp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form.get('role', 'User')
        
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        new_user.role = role
        
        with Session() as session_db:
            session_db.add(new_user)
            session_db.commit()
        return redirect(url_for('user.login'))
    
    return render_template('register.html')