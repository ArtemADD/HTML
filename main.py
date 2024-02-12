from flask import *

app = Flask(__name__)


@app.route('/')
def main():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    words = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
             'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(words)


@app.route('/image_mars')
def return_mars_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/MARS.png')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                    <h3>Вот она какая, красная планета.</h3>
                  </body>
                </html>"""


@app.route('/promotion_image')
def return_promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/MARS.png')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-dark">
                        <h3>Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success">
                        <h3>Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary">
                        <h3>Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning">
                        <h3>И начнем с Марса!
                    </div>
                    <div class="alert alert-danger">
                        <h3>Присоединяйся!
                    </div>
                  </body>
                </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h2>Анкета претендента</h2>
                            <h3>на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <label for="email"></label>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                    <label for="prof">Какие у Вас профессии?</label>
                                    <div class="form-group form-check" id="prof">
                                        <div>
                                            <input type="checkbox" class="form-check-input" id="inj-is" name="1">
                                            <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" class="form-check-input" id="inj-str" name="2">
                                            <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" class="form-check-input" id="pilot" name="3">
                                            <label class="form-check-label" for="acceptRules">Пилот</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" class="form-check-input" id="meteo" name="4">
                                            <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" class="form-check-input" id="inj-hel" name="5">
                                            <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" class="form-check-input" id="inj-rad" name="6">
                                            <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" class="form-check-input" id="doctor" name="7">
                                            <label class="form-check-label" for="acceptRules">Врач</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" class="form-check-input" id="biolog" name="8">
                                            <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите поучаствовать в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['name'])
        print(request.form['surname'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['accept'])
        return "Форма отправлена"


@app.route('/choice/<planet>')
def choice(planet):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Моё предложение: {planet}</h1>
                    <h2>Эта планета близка к земле;</h2>
                    <div class="alert alert-success">
                        <h2>На ней много необходимых ресурсов;
                    </div>
                    <div class="alert alert-secondary">
                        <h2>На ней есть вода и атмосфера;
                    </div>
                    <div class="alert alert-warning">
                        <h2>На ней есть небольшое магнитное поле;
                    </div>
                    <div class="alert alert-danger">
                        <h2>Наконец, она просто красивая!
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
