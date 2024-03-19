from flask import Flask, request, render_template
from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/', methods=['POST', 'GET'])
def load_file():
    if request.method == 'GET':
        return render_template('2.html')
    elif request.method == 'POST':
        load_img(request.files['file'])
        return render_template('2.html')


def load_img(file):
    with open('static/img/img.png', "wb") as f:
        f.write(file.read())


def main():
    app.run()


if __name__ == '__main__':
    main()
