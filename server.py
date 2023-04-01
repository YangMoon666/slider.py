from flask import Flask, render_template, request
import os


app = Flask(__name__)
os.chdir('static//img')


@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        files = os.listdir(path=".")
        return render_template('index.html', title='Карусель', files=files[1:])
    elif request.method == 'POST':
        img = request.files['file']
        img.save(img.filename)
        return 'Файл успешно загружен, обновите страницу'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')