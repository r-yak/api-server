import http

import flask


app = flask.Flask(__name__)


@app.get('/')
def index():
    return flask.Response(response='Hello, world!', status=http.HTTPStatus.OK)


if __name__ == '__main__':
    # 터미널에서 다음의 명령으로도 실행 가능:
    # flask --app src/app.py --debug run --port 8000
    app.run(port=8000, debug=True)
