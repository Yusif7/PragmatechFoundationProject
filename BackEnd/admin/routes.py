from flask import Blueprint,render_template,redirect,request
from app import db
from . forms import AboutForm, BlogForm, SkillForm, CategoryForm, WorksForm
from app.models import *
import os
import random
from datetime import date


admin=Blueprint(
    'admin',
    __name__,
    url_prefix='/admin',
    template_folder='templates',
    static_folder='static')

@admin.route('/')
def adminIndex():
    return render_template('layout.html')

# ROUTES FOR ABOUT

@admin.route('/about')
def about():
    about = About.query.all()
    return render_template('About/about.html',about=about)

@admin.route('/about/add', methods=['GET', 'POST'])
def addAbout():
    aboutform = AboutForm()
    if request.method == 'POST':
        file = aboutform.about_img.data
        file.save(file.filename)
        about = About (
            about_title = aboutform.about_title.data,
            about_img = file.filename,
            about_content = aboutform.about_content.data,
            about_date = date.today()
        )
        db.session.add(about)
        db.session.commit()
        return redirect ('/admin/about')
    return render_template('About/add.html', form=aboutform)

@admin.route('/about/update/<int:id>', methods=['GET', 'POST'])
def updateAbout(id):
    about = About.query.get(id)
    aboutform = AboutForm()
    if request.method == 'POST':
        file = aboutform.about_img.data
        file.save(file.filename)
        newTitle = aboutform.about_title.data
        newImg = file.filename
        newContent = aboutform.about_content.data
        about.about_title = newTitle
        about.about_img = newImg
        about.about_content = newContent
        db.session.merge(about)
        db.session.flush()
        db.session.commit()
        return redirect ('/admin/about')
    return render_template('About/update.html', form=aboutform, about=about)

@admin.route('/about/delete/<int:id>')
def deleteAbout(id):
    about = About.query.get(id)
    db.session.delete(about)
    db.session.commit()
    return redirect ('/admin/about')

# END OF ROUTES FOR ABOUT 

# ROUTES FOR BLOG

@admin.route('/blog')
def blog():
    blogs = Blog.query.all()
    return render_template('Blog/blog.html',blogList=blogs)

@admin.route('/blog/add', methods=['GET', 'POST'])
def addBlog():
    blogform = BlogForm()
    if request.method == 'POST':
        file = blogform.blog_img.data
        file.save(file.filename)
        blog = Blog (
            blog_title = blogform.blog_title.data,
            blog_img = file.filename,
            blog_content = blogform.blog_content.data,
            blog_author = blogform.blog_author.data,
            blog_status = blogform.blog_status.data,
            blog_date = date.today()
        )
        db.session.add(blog)
        db.session.commit()
        return redirect ('/admin/blog')
    return render_template('Blog/add.html', form=blogform)

@admin.route('/blog/update/<int:id>', methods=['GET', 'POST'])
def updateBlog(id):
    blog = Blog.query.get(id)
    blogform = BlogForm()
    if request.method == 'POST':
        file = blogform.blog_img.data
        file.save(file.filename)
        newTitle = blogform.blog_title.data
        newImg = file.filename
        newContent = blogform.blog_content.data
        newAuthor = blogform.blog_author.data
        newStatus = blogform.blog_status.data
        blog.blog_title = newTitle
        blog.blog_img = newImg
        blog.blog_content = newContent
        blog.blog_author = newAuthor
        blog.blog_status = newStatus
        db.session.merge(blog)
        db.session.flush()
        db.session.commit()
        return redirect ('/admin/blog')
    return render_template('Blog/update.html', form=blogform, blog=blog)

@admin.route('/blog/delete/<int:id>')
def deleteBlog(id):
    blog = Blog.query.get(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect ('/admin/blog')


# END OF ROUTES FOR BLOG 

# ROUTES FOR SKILL

@admin.route('/skill')
def skill():
    skills = Skill.query.all()
    return render_template('Skill/skill.html',skillList=skills)

@admin.route('/skill/add', methods=['GET', 'POST'])
def addskill():
    skillform = SkillForm()
    if request.method == 'POST':
        skill = Skill (
            skill_title = skillform.skill_title.data,
            skill_icon = skillform.skill_icon.data,
            skill_content = skillform.skill_content.data,
            skill_status = skillform.skill_status.data,
            skill_date = date.today()
        )
        db.session.add(skill)
        db.session.commit()
        return redirect ('/admin/skill')
    return render_template('Skill/add.html', form=skillform)

@admin.route('/skill/update/<int:id>', methods=['GET', 'POST'])
def updateSkill(id):
    skill = Skill.query.get(id)
    skillform =SkillForm()
    if request.method == 'POST':
        newTitle = skillform.skill_title.data
        newContent = skillform.skill_content.data
        newIcon = skillform.skill_icon.data
        newStatus = skillform.skill_status.data
        skill.skill_title = newTitle
        skill.skill_content = newContent
        skill.skill_icon = newIcon
        skill.skill_status = newStatus
        db.session.merge(skill)
        db.session.flush()
        db.session.commit()
        return redirect ('/admin/skill')
    return render_template('Skill/update.html', form=skillform, skill=skill)

@admin.route('/skill/delete/<int:id>')
def deleteSkill(id):
    skill = Skill.query.get(id)
    db.session.delete(skill)
    db.session.commit()
    return redirect ('/admin/skill')

# END OF ROUTE OO SKILL

# ROUTES FOR CONTACT

@admin.route('/contact')
def contact():
    contacts = Contact.query.all()
    return render_template('Contact/contact.html',contactList=contacts)

@admin.route('/contact/delete/<int:id>')
def deleteContact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect ('/admin/contact')


# END OF ROUTES FOR CONTACT

# ROUTES FOR BLOG REPLY

@admin.route('/reply')
def reply():
    replies = BlogReply.query.all()
    return render_template('BlogReply/reply.html',replyList=replies)

@admin.route('/reply/delete/<int:id>')
def deleteReply(id):
    reply = BlogReply.query.get(id)
    db.session.delete(reply)
    db.session.commit()
    return redirect ('/admin/reply')

# END OF ROUTES FOR BLOG REPLY

# ROUTES FOR WORKS CATEGORY

@admin.route('/works/categories')
def categories():
    categories = Category.query.all()
    return render_template('Works/Category/categories.html',categoryList=categories)

@admin.route('/works/categories/add', methods=['GET', 'POST'])
def addCategory():
    categoryform = CategoryForm()
    if request.method == 'POST':
        category = Category (
            category_data = categoryform.category_data.data,
            category_name = categoryform.category_name.data,
            category_all = categoryform.category_all.data
        )
        db.session.add(category)
        db.session.commit()
        return redirect ('/admin/works/categories')
    return render_template('Works/Category/add.html', form=categoryform)

@admin.route('/works/categories/update/<int:id>', methods=['GET', 'POST'])
def updateCategory(id):
    category = Category.query.get(id)
    categoryform = CategoryForm()
    if request.method == 'POST':
        newData = categoryform.category_data.data
        newName = categoryform.category_name.data
        newAll = categoryform.category_all.data
        category.category_data = newData
        category.category_name = newName
        category.category_all = newAll
        db.session.merge(category)
        db.session.flush()
        db.session.commit()
        return redirect ('/admin/works/categories')
    return render_template('Works/Category/update.html', form=categoryform, category=category)

@admin.route('/works/categories/delete/<int:id>')
def deleteCategory(id):
    category = Category.query.get(id)
    db.session.delete(category)
    db.session.commit()
    return redirect ('/admin/works/categories')

# END OF ROUTES FOR WORKS CATEGORY

# ROUTES FOR WORKS

@admin.route('/works')
def works():
    works = Works.query.all()
    return render_template('Works/works.html',workList=works)

@admin.route('/works/add', methods=['GET', 'POST'])
def addworks():
    worksform = WorksForm()
    if request.method == 'POST':
        file = worksform.work_img.data
        file.save(file.filename)
        works = Works (
            work_title = worksform.work_title.data,
            work_img = file.filename,
            work_content = worksform.work_content.data,
            work_status = worksform.work_status.data,
            work_class = worksform.work_class.data,
            work_data = worksform.work_data.data,
            work_brand = worksform.work_brand.data,
            work_date = date.today(),
            categoryId = worksform.categories.data
        )
        db.session.add(works)
        db.session.commit()
        return redirect ('/admin/works')
    return render_template('Works/add.html', form=worksform)

# END OF ROUTES FOR WORKS
