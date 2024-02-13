from flask import *

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Заголовок')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
