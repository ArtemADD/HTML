from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    tm = list(map(lambda x: x.id, jobs))
    users = db_sess.query(User.id,User.surname, User.name).where(User.id.in_(tm)).all()
    tms = {v[0]: f'{v[1]} {v[2]}' for v in users}
    print(tms)
    return render_template("index.html", jobs=jobs, tm=tms)


def main():
    db_session.global_init('db/mars_explorer.db')
    app.run()


if __name__ == '__main__':
    main()
