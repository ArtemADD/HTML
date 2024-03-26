from flask import Flask, render_template, request, redirect, abort, make_response, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data.users import User
from data.jobs import Jobs
from data.departments import Department
from data.category import Category
from forms.user import RegisterForm, LoginForm, Zxc
from forms.jobs import JobsForm
from forms.departments import DepartmentsForm
from data import db_session, jobs_api, users_api
import os
from random import randint
from io import BytesIO
from requests import get


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/distribution')
def distribution():
    zxc = ['zxc', 'asdsd', 'dgfgj', 'vvbnv', 'rytryr', 'qeweq']
    return render_template('2.html', data=zxc)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Registration',
                                   form=form,
                                   message="Passwords don't match")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Registration',
                                   form=form,
                                   message="There is already such a user")
        user = User(
            email=form.email.data,
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position = form.position.data,
            speciality = form.speciality.data,
            address = form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Registration', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Zxc()
    if form.validate_on_submit():
        return redirect("/")
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/")
def index():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        jobs = db_sess.query(Jobs).all()
        tm = list(map(lambda x: x.id, jobs))
        users = db_sess.query(User.id, User.surname, User.name).where(User.id.in_(tm)).all()
        tms = {v[0]: f'{v[1]} {v[2]}' for v in users}
    else:
        jobs = db_sess.query(Jobs).all()
        tm = list(map(lambda x: x.id, jobs))
        users = db_sess.query(User.id, User.surname, User.name).where(User.id.in_(tm)).all()
        tms = {v[0]: f'{v[1]} {v[2]}' for v in users}
    return render_template("index.html", jobs=jobs, tm=tms)


@app.route('/jobs',  methods=['GET', 'POST'])
@login_required
def add_jobs():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = Jobs()
        jobs.job = form.job.data
        jobs.team_leader = form.team_leader.data
        jobs.work_size = form.work_size.data
        jobs.collaborators = form.collaborators.data
        jobs.categories.append(db_sess.query(Category).filter(Category.id == form.category.data).first())
        jobs.is_finished = form.is_finished.data
        db_sess.add(jobs)
        db_sess.commit()
        return redirect('/')
    return render_template('jobs.html', title='Adding a job',
                           form=form, label='Adding a job')


@app.route('/jobs/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_jobs(id):
    form = JobsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id).first()
        if jobs:
            form.job.data = jobs.job
            form.team_leader.data = jobs.team_leader
            form.work_size.data = jobs.work_size
            form.collaborators.data = jobs.collaborators
            form.category.data = jobs.categories[0].name
            form.is_finished.data = jobs.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).filter(Jobs.id == id).first()
        if jobs:
            jobs.job = form.job.data
            jobs.team_leader = form.team_leader.data
            jobs.work_size = form.work_size.data
            jobs.collaborators = form.collaborators.data
            jobs.categories.append(db_sess.query(Category).filter(Category.id == form.category.data).first())
            jobs.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('jobs.html',
                           title='Editing a job',
                           form=form, label='Editing a job'
                           )


@app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def jobs_delete(id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.id == id).first()
    if jobs:
        db_sess.delete(jobs)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/users_show/<int:user_id>')
def user_show(user_id):
    user = get(f'http://localhost:5000/api/users/{user_id}').json()['user']
    c = user['city_from']
    response = get(f'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode="{c}"&format=json').json()
    if not response:
        return response
    pos = ','.join(response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split())
    response = get(f'http://static-maps.yandex.ru/1.x/?ll={pos}&spn=0.09,0.09&l=sat')
    with open('static/img/map.png', 'wb+') as f:
        f.write(response.content)
    return render_template('shows.html', user=user)


@app.route('/departments')
def departments_index():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        departments = db_sess.query(Department).all()
        chiefs = list(map(lambda x: x.chief, departments))
        users = db_sess.query(User.id, User.surname, User.name).where(User.id.in_(chiefs)).all()
        tms = {v[0]: f'{v[1]} {v[2]}' for v in users}
    else:
        departments = []
        tms = []
    return render_template("departments_index.html", departments=departments, tm=tms)


@app.route('/new_department', methods=['GET', 'POST'])
@login_required
def new_department():
    form = DepartmentsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        department = Department()
        department.title = form.title.data
        department.chief = form.chief.data
        department.members = form.members.data
        department.email = form.email.data
        db_sess.add(department)
        db_sess.commit()
        return redirect('/departments')
    return render_template('new_departments.html', title='Adding a department',
                           form=form, label='Adding a department')


@app.route('/department/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    form = DepartmentsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        department = db_sess.query(Department).filter(Department.id == id).first()
        if department:
            form.title.data = department.title
            form.chief.data = department.chief
            form.members.data = department.members
            form.email.data = department.email
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        department = db_sess.query(Department).filter(Department.id == id).first()
        if department:
            department.title = form.title.data
            department.chief = form.chief.data
            department.members = form.members.data
            department.email = form.email.data
            db_sess.commit()
            return redirect('/departments')
        else:
            abort(404)
    return render_template('new_departments.html',
                           title='Editing a department',
                           form=form, label='Editing a department'
                           )


@app.route('/department_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def department_delete(id):
    db_sess = db_session.create_session()
    department = db_sess.query(Department).filter(Department.id == id).first()
    if department:
        db_sess.delete(department)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/departments')


def main():
    db_session.global_init('db/mars_explorer.db')
    app.register_blueprint(jobs_api.blueprint)
    app.register_blueprint(users_api.blueprint)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


if __name__ == '__main__':
    main()
