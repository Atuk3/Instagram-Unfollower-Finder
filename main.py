import json
import os
from flask import Flask,render_template, request, jsonify,flash,url_for,redirect
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
    form =UploadFileForm()
    
    if form.validate_on_submit():
        file=form.file.data
        file2=form.file2.data
        if file.filename != "followers.json": 
            flash("Invalid file for Followers.")
            return render_template('index.html', form=form)
            
        if file2.filename != "following.json":
             flash("Invalid file for Following.")
             return render_template('index.html', form=form)
            
        
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        file2.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'], secure_filename(file2.filename)))
        
        
        return redirect(url_for('compare_list'))
    
    return render_template('index.html', form=form)


@app.route('/compare', methods=['GET', 'POST'])
def compare_list():
   
    followers_values = []
    following_values = []
    with open ('static/files/followers.json') as json_file:
        data=json.load(json_file)
    #iterate through the relationships_followers list
    for relationship in data['relationships_followers']:
        # iterate through the string_list_data list
        for string_data in relationship['string_list_data']:
            # append the value to the values array
            followers_values.append(string_data['value'])

    with open ('static/files/following.json') as json_file:
        data=json.load(json_file)
   # iterate through the relationships_followers list
    for relationship in data['relationships_following']:
        # iterate through the string_list_data list
        for string_data in relationship['string_list_data']:
            # append the value to the values array
             following_values.append(string_data['value'])
   
    not_in_followers = []
    for val in following_values:
        if val not in followers_values:
            not_in_followers.append(val)
    return render_template('compare.html', not_in_followers=not_in_followers)

if __name__ == '__main__':
    app.run(debug=true)