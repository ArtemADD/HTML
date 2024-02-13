from flask import *

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
