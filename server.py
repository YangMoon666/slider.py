from flask import Flask, url_for, request


app = Flask(__name__)


IMG_KEY = 0


@app.route('/', methods=['POST', 'GET'])
def sample_file_upload():
    global IMG_KEY
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Марс</title>
                          </head>
                          <body>
                            <form class="form" method="post" enctype="multipart/form-data">
                                <img src="{url_for('static', filename=f'img/mars.{IMG_KEY}.jpg')}" width="500" height="390" 
                                alt="здесь должна была быть картинка, но не нашлась">

                                <button type="submit" class="btn btn-primary">Следующая</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        IMG_KEY += 1
        IMG_KEY %= 5
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                            <title>Марс</title>
                          </head>
                          <body>
                            <form class="form" method="post" enctype="multipart/form-data">
                                <img src="{url_for('static', filename=f'img/mars.{IMG_KEY}.jpg')}" width="500" height="390" 
                                alt="здесь должна была быть картинка, но не нашлась">

                                <button type="submit" class="btn btn-primary">Следующая</button>
                            </form>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')