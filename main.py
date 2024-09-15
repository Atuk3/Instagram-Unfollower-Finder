import json
import os
from flask import Flask,render_template, request, jsonify,flash,url_for,redirect,session
from sqlalchemy import true
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired


app=Flask(__name__)
app.config['SECRET_KEY']='david'
app.config['UPLOAD_FOLDER']='static/files'


class UploadFileForm(FlaskForm):
    file=FileField("Followers", validators=[InputRequired()])
    file2=FileField("Following", validators=[InputRequired()])
    submit=SubmitField("Compare")


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])

def home():
    form = UploadFileForm()

    if form.validate_on_submit():
        file = form.file.data
        file2 = form.file2.data

        if file.filename != "followers.json" and file.filename != "followers_1.json" :
            flash('Invalid file for Followers.', category='error')
            return redirect(url_for('home'))
        if file2.filename != "following.json":
            flash('Invalid file for Following.', category='error')
            return redirect(url_for('home'))

        else:
            # Read the contents of the files into memory
            followers_data = json.loads(file.read())
            following_data = json.loads(file2.read())

            followers_values = []
            followers_link = []
            following_values = []
            following_link = []
            if file.filename=="followers.json":
                #iterate through the relationships_followers list
                for relationship in followers_data['relationships_followers']:
                    # iterate through the string_list_data list
                    for string_data in relationship['string_list_data']:
                        # append the value to the values array
                        followers_values.append(string_data['value'])
                        followers_link.append(string_data['href'])
                       
            

            if file.filename=="followers_1.json":
            #iterate through the relationships_followers list
                for relationship in followers_data:
                    # iterate through the string_list_data list
                    for string_data in relationship['string_list_data']:
                        # append the value to the values array
                        followers_values.append(string_data['value'])
                        followers_link.append(string_data['href'])

            # iterate through the relationships_followers list
            for relationship in following_data['relationships_following']:
                # iterate through the string_list_data list
                for string_data in relationship['string_list_data']:
                    # append the value to the values array
                    following_values.append(string_data['value'])
                    following_link.append(string_data['href'])

            not_in_followers = []
            not_in_followers_link = []
            for val in following_values:
                if val not in followers_values:
                    not_in_followers.append(val)

            for non_follower in not_in_followers:
                index = following_values.index(non_follower)
                not_in_followers_link.append(following_link[index])
            return render_template('compare.html', not_in_followers=not_in_followers, not_in_followers_link=not_in_followers_link)

    return render_template('index.html', form=form)

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/tutorial', methods=['GET', 'POST'])
def tutorial():
    return render_template('tutorial.html')

@app.route('/termsofservice', methods=['GET', 'POST'])
def termsofservice():
    return render_template('termsofservice.html')

@app.route('/privacypolicy', methods=['GET', 'POST'])
def privacypolicy():
    return render_template('privacypolicy.html')

@app.route('/faqs', methods=['GET', 'POST'])
def faqs():
    return render_template('faqs.html')


if __name__ == '__main__':
    app.run(debug=true)