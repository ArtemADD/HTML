from flask import *
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Заголовок')


@app.route('/training/<prof>')
def training(prof):
    return render_template('2.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('3.html', list=list)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    param = {}
    param['title'] = 'Анкета'
    param['surname'] = 'Watny'
    param['name'] = 'Mark'
    param['education'] = 'выше среднего'
    param['profession'] = 'штурман марсохода'
    param['sex'] = 'male'
    param['motivation'] = 'Всегда мечтал застрять на марсе!'
    param['ready'] = 'True'
    return render_template('auto_answer.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
