from flask import Blueprint,render_template,redirect,request
from app.forms import ContactForms

blogs=Blueprint(
    'blog',
    __name__,
    url_prefix='/blog',
    template_folder='templates',
    static_folder='static')

@blogs.route('/')
def blogndex():
    form=ContactForms()
    return render_template('blogMain.html',form=form)

@blogs.route('/single')
def single():
    return render_template ('blogSingle.html')