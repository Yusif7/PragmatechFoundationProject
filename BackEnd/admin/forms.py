from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField,TextAreaField,FileField

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

