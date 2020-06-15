from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm

# Initialiazation
app = Flask(__name__)
app.config['SECRET_KEY'] = '801f07f84422bbfe0bc2edce21c63ff7'

myBlogs = [
        {
                'title':'Why Python',
                'content':'Python is High Level Programming Language',
                'author':'Onkar Nardekar',
                'timeStamp':'12th June, 2020'
        },
        {
                'title':'Top 2 Python Frameworks',
                'content':'Top 2 Python Framworks are Django and Flask Respectivily',
                'author':'Onkar Nardekar',
                'timeStamp':'13th June, 2020'
        },
       {
                'title':'Gym Abs workout',
                'content':'Abs workout is Very difficult, so leave it and Go buy some delicious Food to Eat, We all get one life so Enjoy',
                'author':'Onkar Nardekar',
                'timeStamp':'14th June, 2020'
        },
]

@app.route('/')
@app.route('/home')
def indexHome():
        return render_template('blog/index.html', blogs=myBlogs)

@app.route('/register', methods=['GET','POST'])
def register():
        forms = RegistrationForm()
        if forms.validate_on_submit():
                flash(f'Your Account has been Created {forms.username.data}!', 'success')
                return redirect(url_for('indexHome'))
        return render_template('user/register.html', forms=forms)

if __name__ == '__main__':
        app.run(debug=True)