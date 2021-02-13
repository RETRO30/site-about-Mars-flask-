from flask import Flask
from flask import url_for

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
