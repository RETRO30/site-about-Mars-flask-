from flask import Flask
from flask import url_for
from flask import request

app = Flask(__name__)


@app.route('/')
def start_page():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    strings = ["Человечество вырастает из детства.",
               "Человечеству мала одна планета.",
               "Мы сделаем обитаемыми безжизненные пока планеты.",
               "И начнем с Марса!",
               "Присоединяйся!"]
    return "</br>".join(strings)


@app.route('/image_mars')
def image_mars():
    data = f"""<html><head>
    <title>Привет, Марс!</title>
    </head>
    <body><h1>Жди нас, Марс!</h1>
    <p><img src="{url_for('static', filename='img/mars_image_1.png')}" alt="здесь должна была быть картинка, но не нашлась">
    <br>Вот она какая, красная планета.</br></p></body>
    </html>"""
    return data


@app.route('/promotion_image')
def promotion_image():
    data = f"""<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Привет, Марс!</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
            <p>
                <img src="{url_for('static', filename='img/mars_image_1.png')}" alt="здесь должна была быть картинка, но не нашлась">
                <div class="alert alert-dark" role="alert"><strong>Человечество вырастает из детства.</strong></div>
                <div class="alert alert-success" role="alert"><strong>Человечеству мала одна планета.</strong></div>
                <div class="alert alert-secondary" role="alert">
                    <strong>Мы сделаем обитаемыми безжизненные пока планеты.</strong>
                </div>
                <div class="alert alert-warning" role="alert"><strong>И начнем с Марса!</strong></div>
                <div class="alert alert-danger" role="alert"><strong>Присоединяйся!</strong></div>
            </p>
    </body>
</html>
"""
    return data


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    if request.method == 'GET':
        data = open('astronaut_selection.html', encoding='utf8').read()
        return data
    elif request.method == 'POST':
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
