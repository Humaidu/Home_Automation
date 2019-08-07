from flask import Flask, render_template, url_for, flash, redirect
from forms import * 
from models import *


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

#database configure
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://iztzzjfimduxti:2158361de83d1ef48b8e3a723fd0882ab88245cf2a48a379143887e4b2fef847@ec2-107-21-120-104.compute-1.amazonaws.com:5432/ddajc1h5rt70a7'

db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')


@app.route("/register", methods=['GET', 'POST'])
def register():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():

        username = reg_form.username.data
        email = reg_form.email.data
        contact = reg_form.contact.data
        password = reg_form.password.data
        

        #check username exist
        user_object = User.query.filter_by(username = username).first()
        if user_object:
            return "Someone has taken this username"
        
        #add users
        user = User(username = username,email = email,contact = contact, password=password)
        db.session.add(user)
        db.session.commit()
        # flash(f'Account created for {reg_form.username.data}!', 'success')
        # return redirect(url_for('register'))
        return "Inserted Into Database"
    return render_template('register.html', title='Register', form=reg_form)



if __name__ == '__main__':
    app.run(debug=True)