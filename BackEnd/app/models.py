# For createing tables we database class
from app import db
from datetime import date

# ABOUT MODEL

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    about_title = db.Column(db.String(80), nullable=False)
    about_img = db.Column(db.String(50), nullable=False)
    about_content = db.Column(db.Text, nullable=False)
    about_date = db.Column(db.DateTime)

# END OF ABOUT MODEL

# WHAT I DO MODEL

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill_title = db.Column(db.String(50), nullable=False)
    skill_content = db.Column(db.Text, nullable=False)
    skill_icon = db.Column(db.String(50), nullable=False)
    skill_date = db.Column(db.DateTime)
    skill_status = db.Column(db.String(10), nullable=False)

# END OF WHAT I DO MODEL

# BLOG MODEL

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(80), nullable=False)
    blog_img = db.Column(db.String(50), nullable=False)
    blog_content = db.Column(db.Text, nullable=False)
    blog_author = db.Column(db.String(50), nullable=False)
    blog_date = db.Column(db.DateTime)
    blog_status = db.Column(db.String(10), nullable=False)

# END OF BLOG MODEL

# WORKS MODEL

class Works(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    work_title = db.Column(db.String(80), nullable=False)
    work_img = db.Column(db.String(50), nullable=False)
    work_class = db.Column(db.String(20), nullable=False)
    work_data = db.Column(db.String(20), nullable=False)
    work_content = db.Column(db.Text, nullable=False)
    work_brand = db.Column(db.String(50), nullable=False)
    work_status = db.Column(db.String(10), nullable=False)
    work_date = db.Column(db.DateTime)

# END OF WORKS MODEL

# WORKS CATEGORY

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_data = db.Column(db.String(30), nullable=False)
    category_name = db.Column(db.String(30), unique=True, nullable=False)
    category_all = db.Column(db.String(30), nullable=False)
# END OF WORKS CATEGORY


# CONTACT MODEL

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_name = db.Column(db.String(30), nullable=False)
    contact_phone = db.Column(db.String(50), nullable=False)
    contact_email = db.Column(db.String(50), nullable=False)
    contact_subject = db.Column(db.String(50), nullable=False)
    contact_message = db.Column(db.Text, nullable=False)
    contact_date = db.Column(db.DateTime)

# END OF CONTACT MODEL

# SINGLE BLOG

class BlogComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blogComment_name = db.Column(db.String(30), nullable=False)
    blogComment_content = db.Column(db.Text, nullable=False)
    blogComment_date = db.Column(db.DateTime)

#END OF SINGLE BLOG

# BLOG COMMENT REPLY

class BlogReply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blogReply_name = db.Column(db.String(30), nullable=False)
    blogReply_email = db.Column(db.String(40), nullable=False)
    blogReply_content = db.Column(db.Text, nullable=False)
    blogReply_date = db.Column(db.DateTime)

# END OF BLOG COMMENT REPLY