from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Regexp
from flask_bootstrap import Bootstrap5


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False
bootstrap = Bootstrap5(app)


all_books = []

class LibraryForm(FlaskForm):
    book_name = StringField('name', validators=[DataRequired()])
    author = StringField('name', validators=[DataRequired()])
    rating = SelectField(
        'Choose an rating',
        choices=[
            ('⭐', '⭐'),
            ('⭐⭐', '⭐⭐'),
            ('⭐⭐⭐', '⭐⭐⭐'),
            ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
            ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')
        ], validators=[DataRequired()])
    submit = SubmitField('Submit')



@app.route('/')
def home():
    return render_template('index.html', lib_books=all_books)


@app.route("/add", methods=['GET','POST'])
def add():
    lib_form = LibraryForm()
    if lib_form.validate_on_submit():
        book_name = lib_form.book_name.data
        author = lib_form.author.data
        rating = lib_form.rating.data
        # You can append the book details to your all_books list or handle them as needed
        all_books.append({'name': book_name, 'author': author, 'rating': rating})
        print(all_books)
        return redirect(url_for('home'))  # Redirect after successful submission
    return render_template('add.html', form=lib_form)


if __name__ == "__main__":
    app.run(debug=True)

