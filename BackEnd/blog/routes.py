from flask import Blueprint,render_template,redirect,request
from app.models import BlogReply, Blog, BlogComment, Works
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
    blogs = Blog.query.limit(6).all()
    return render_template('blog_main.html', blogList = blogs)

@blogs.route('/single', methods=['GET', 'POST'])
def single():
    blogReply = BlogReply.query.all()
    work = Works.query.limit(3).all()
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
    return render_template ('blog_inner.html', replyList = blogReply, workList = work)

