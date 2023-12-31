import base64
import http

import cv2
import flask
import numpy


API_VERSION = 1
API_BASEURL = f'/api/v{API_VERSION}'

ALLOWED_IMAGE_SIZE = 256


app = flask.Flask(__name__)


@app.post(API_BASEURL)
def index():
    app.logger.info(f'data received (length: {len(flask.request.data)})')

    # Base 64 문자열로 들어온 이미지를 복호화
    bytes_img = base64.b64decode(flask.request.data)
    numpy_img = numpy.fromstring(bytes_img, dtype=numpy.uint8)
    bgr_image = cv2.imdecode(numpy_img, cv2.IMREAD_COLOR)

    # 이미지를 제대로 전달 받았는지 확인
    app.logger.debug('요청으로 받은 이미지를 input.png 로 저장하고 있습니다.')
    cv2.imwrite('input.png', bgr_image)

    # 이미지의 크기가 256 x 256 인 경우에만 진행
    assert bgr_image.shape[0] == ALLOWED_IMAGE_SIZE and bgr_image.shape[1] == ALLOWED_IMAGE_SIZE

    return flask.Response(status=http.HTTPStatus.OK)


if __name__ == '__main__':
    # 터미널에서 다음의 명령으로도 실행 가능:
    # flask --app src/app.py --debug run --port 8000
    app.run(port=8000, debug=True)
