# We import app class from app package because we app route
from app import app,db
from flask import render_template, redirect, request, url_for
from . models import *
# We import forms file from route because we want ad forms to our html pages
#from flask import Blueprint
import os
import random
from datetime import date

@app.route("/", methods=['GET', 'POST'])
def home():
    about = About.query.all()
    skill = Skill.query.all()
    blog = Blog.query.all()
    category = Category.query.all()
    work = Works.query.all()
    if request.method == 'POST':
        contact = Contact (
            contact_name = request.form['name'],
            contact_phone = request.form['tel'],
            contact_email = request.form['email'],
            contact_subject = request.form['subject'],
            contact_message = request.form['message'],
            contact_date = date.today()
        )
        db.session.add(contact)
        db.session.commit()
        return redirect ("/")
    return render_template ('index.html', aboutList=about,skillList = skill, blogList = blog, categoryList = category, workList = work)
