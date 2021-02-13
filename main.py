from flask import Flask

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
    data = """<html><head>
    <title>Привет, Марс!</title>
    </head>
    <body><h1>Жди нас, Марс!</h1>
    <p></p></body>
    </html>"""
    return data

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
