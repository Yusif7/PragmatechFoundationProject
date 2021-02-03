from flask import Blueprint,render_template,redirect,request
from app.models import BlogReply
from datetime import date
from app import db

blogs=Blueprint(
    'blog',
    __name__,
    url_prefix='/blog',
    template_folder='templates',
    static_folder='static')

@blogs.route('/')
def blogndex():
    return render_template('blog_main.html')

@blogs.route('/single', methods=['GET', 'POST'])
def single():
    if request.method == 'POST':
        blogReply = BlogReply (
            blogReply_name  = request.form['name'],
            blogReply_content = request.form['message'],
            blogReply_email = request.form['email'],
            blogReply_date = date.today()
        )
        db.session.add(blogReply)
        db.session.commit()
        return redirect ("/blog/single")
    return render_template ('blog_inner.html')

