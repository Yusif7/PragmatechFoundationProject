from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField,TextAreaField,FileField
from app.models import Category

# FORMS FOR ABOUT 
class AboutForm(FlaskForm):
    about_title = StringField('Title')
    about_img = FileField('Personal Photo')
    about_content = StringField('About Info')
    submit = SubmitField()

# FORMS FOR BLOG

class BlogForm(FlaskForm):
    blog_title = StringField('Title')
    blog_img = FileField('Photo')
    blog_content = TextAreaField('Content')
    blog_author = StringField('Author')
    blog_status = StringField('Status')
    submit = SubmitField()

# FORMS FOR SKILLS

class SkillForm(FlaskForm):
    skill_title = StringField('Title')
    skill_icon = StringField('Icon')
    skill_content = TextAreaField('Content')
    skill_status = StringField('Status')
    submit = SubmitField()

# FORMS FOR CATEGORY

class CategoryForm(FlaskForm):
    category_data = StringField('Category Data Filter')
    category_name = StringField('Category Name')
    category_all = StringField('All Categories')
    submit = SubmitField()

# FORMS FOR WORKS

class WorksForm(FlaskForm):
    work_brand = StringField('Brand')
    work_class = StringField('Class')
    work_content = StringField('Content')
    work_data = StringField('Data')
    work_title = StringField('Title')
    work_status = StringField('Status')
    work_img = FileField()
    categories = SelectField('CatList', choices=Category.query.with_entities(Category.id, Category.category_name).all())
    submit = SubmitField()
