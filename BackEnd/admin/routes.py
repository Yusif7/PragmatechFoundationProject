from flask import Blueprint,render_template,redirect,request

admin=Blueprint(
    'admin',
    __name__,
    url_prefix='/admin',
    template_folder='templates',
    static_folder='static')

@admin.route('/')
def adminIndex():
    return render_template('admin/index.html')

@admin.route('/users')
def adminSingle():
    return render_template('admin/users.html')