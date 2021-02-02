# We import app class from app package because we app route
from app import app
from flask import render_template, redirect, request, url_for
# We import forms file from route because we want ad forms to our html pages
from . forms import ContactForms
#from flask import Blueprint
import os
import random

# blogs = Blueprint('blog',__name__,url_prefix='/blog')
# blogsS = Blueprint('blogSingle',__name__,url_prefix='/blog')

@app.route("/")
def home():
    return render_template ('index.html')

# @blogs.route("/")
# def blog():
#     form = ContactForms()
#     return render_template('blogMain.html', form=form)

# @blogsS.route('/single')
# def blogSingle():
#     return render_template('blogSingle.html') 


